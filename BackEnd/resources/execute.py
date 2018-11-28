from flask_restful import Resource
from service.bid_match import update_holdings
from models.issuer import IssuerModel
from models.ipo import IpoModel
from models.prices import PriceModel


class Execute(Resource):

    def get(self, name):
        issuer = IssuerModel.find_by_name(name)
        ipo = IpoModel.find_by_issuer(name)
        prices = PriceModel.find_by_issuer_id(issuer.id)
        update_holdings(issuer.id, ipo.shares_offering, prices.minimum_price)
        return {"message": "Orders executed"}, 200

        try:
            issuer = IssuerModel.find_by_name(name)
            ipo = IpoModel.find_by_issuer(name)
            update_holdings(issuer.id, ipo.shares_offering)
            return {"message": "Orders executed"}, 200
        except:
            return {"message": "Failed to execute bids"}, 404