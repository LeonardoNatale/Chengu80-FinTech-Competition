from models.holding import HoldingModel
import psycopg2

def update_holdings(issuer_id, max_shares, minimum_price):
    dic_inv = get_bids(issuer_id, max_shares, minimum_price)
    for bid in dic_inv:
        holdings = HoldingModel(bid[0], bid[3], bid[2], bid[1])
        holdings.save_to_db()
       

def get_bids(issuer_id, max_shares,min_price):
    conn = psycopg2.connect("postgresql://group2:123456@10.240.61.106:5432/group2")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bidz WHERE issuer_id = %s" %str(issuer_id))
    bids = cur.fetchall()
    bids.sort(key= lambda bid: (-bid[3], bid[1]))
    cur.execute("DELETE FROM bidz WHERE issuer_id = %s" %str(issuer_id))
    conn.commit()
    cur.close()
    conn.close()

    shares = 0
    ind = 0
    dic_inv_iss = []
    while shares < max_shares:
        if(ind >= len(bids)):
            break;
        if(bids[ind][3] < min_price):
            continue;
        shares = shares + bids[ind][4]
        # print(shares, " 2")
        if shares > max_shares:
            dic_inv_iss.append([bids[ind][2],issuer_id , (bids[ind][4] - shares + max_shares), bids[ind][3]])
        else:
            dic_inv_iss.append([bids[ind][2], issuer_id , bids[ind][4], bids[ind][3]])
        ind = ind + 1

    return dic_inv_iss
