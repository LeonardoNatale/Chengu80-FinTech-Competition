from flask_restful import Resource, reqparse
from models.ipo import IpoModel
from models.issuer import IssuerModel


class Ipo(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('credit_card_percentage',
                        type = float,
                        required = True,
                        help="This field cannot be blank")

    parser.add_argument('shares_offering',
                        type = int,
                        required = True,
                        help="This field cannot be blank")

    parser.add_argument('market_lot',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('minimum_order',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('call_option',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('put_option',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self, name):
        if IpoModel.find_by_issuer(name):
            return {'message': "User '{}' has already issued an IPO".format(name)}, 400

        data = self.parser.parse_args()
        ipo = IpoModel(name, **data)

        ipo.save_to_db()
        try:
            ipo.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return {"message": "IPO created successfully"}, 201

    def get(self, name):
        issuer = IpoModel.find_by_issuer(name)
        if issuer:
            return issuer.json(name)
        return {"message": "Issuer '{}' has not issued an IPO yet".format(name)}, 400


class Ipos(Resource):
    def get(self):
        ipos = IpoModel.find_all()
        if ipos:
            result = {"invest": []}
            for ipo in ipos:
                issuer_id = ipo.issuer_id
                profile = IssuerModel.find_by_id(issuer_id)
                result['invest'].append(profile.json())
            return result