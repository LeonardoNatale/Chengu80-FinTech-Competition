from flask_restful import Resource, reqparse
from models.holding import HoldingModel
from models.investor import InvestorModel
from models.issuer import IssuerModel
from models.prices import PriceModel


class Price(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('suggested_price',
                        type = float,
                        required = True,
                        help="This field cannot be blank")

    parser.add_argument('minimum_price',
                        type = int,
                        required = True,
                        help="This field cannot be blank")

    parser.add_argument('call_price',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('put_price',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    def post(self, name):
        issuer = IssuerModel.find_by_name(name)
        if not issuer:
            return {'message': "User '{}' has not issued an IPO".format(name)}, 400

        data = self.parser.parse_args()

        try:
            prices = PriceModel(issuer.id, **data)
            prices.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return {"message": "Prices saved successfully"}, 201

    def get(self, name):
        issuer = IssuerModel.find_by_name(name)
        if issuer:
            prices = PriceModel.find_by_issuer_id(issuer.id)
            return prices.json()
        return {'message': "User '{}' has not issued an IPO".format(name)}, 400