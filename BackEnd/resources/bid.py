from flask_restful import Resource, reqparse
from models.bid import BidModel
from models.ipo import IpoModel
from models.investor import InvestorModel
from models.issuer import IssuerModel
from models.prices import PriceModel

class Bid(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('amount',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('issuer',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self, investor):
        if not InvestorModel.find_by_username(investor):
            return {"message": "Investor '{}' is not registered".format(investor)}, 400

        data = self.parser.parse_args()
        if not IpoModel.find_by_issuer(data['issuer']):
            return {"message": "'{}' has not issued an IPO yet".format(data['issuer'])}, 400

        issuer_name = data['issuer']
        ipo = IpoModel.find_by_issuer(issuer_name)
        market_lot = ipo.market_lot
        minimum_order = ipo.minimum_order
        bid = BidModel(investor, **data)
        if bid.amount % market_lot != 0 or bid.amount < minimum_order:
            return {"message": "Invalid bid"}
        try:
            bid.save_to_db()
        except:
            return {"message": "Unable to process the bid"}, 500
        return {"message": "Bid saved successfully"}


class Bids(Resource):

    def get(self, investor):
        if not InvestorModel.find_by_username(investor):
            return {"message": "Investor '{}' is not registered".format(investor)}, 400

        investor_id = InvestorModel.find_by_username(investor).id
        result = {"current_bids": []}
        for i in BidModel.find_by_investor_id(investor_id):
            name = IssuerModel.find_by_id(i.issuer_id).name
            price = i.price
            amount = i.amount
            result['current_bids'].append({"name": name, "price": price, "amount": amount})
        return result


class ExecuteBids(Resource):

    def get(self):
        pass