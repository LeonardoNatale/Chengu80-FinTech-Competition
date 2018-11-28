from flask_restful import Resource, reqparse
from models.holding import HoldingModel
from models.investor import InvestorModel
from models.issuer import IssuerModel


class Holdings(Resource):
    def get(self, investor):
        if not InvestorModel.find_by_username(investor):
            return {"message": "Investor '{}' is not registered".format(investor)}, 400

        investor_id = InvestorModel.find_by_username(investor).id
        result = {"portfolio": []}
        for i in HoldingModel.find_by_investor_id(investor_id):
            name = IssuerModel.find_by_id(i.issuer_id).name
            price = i.price
            amount = i.amount
            result['portfolio'].append({"name": name, "price": price, "amount": amount})
        return result

