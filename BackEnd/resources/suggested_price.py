from flask_restful import Resource
from models.issuer import IssuerModel
from models.ipo import IpoModel
from service.controller import Controller

class SuggestedPrice(Resource):
    controller = Controller()
    print(controller)
    ols = controller.train()

    def get(self, name):
        issuer = IssuerModel.find_by_name(name)
        if not issuer:
            return {"message": "Issuer '{}' is not registered".format(issuer)}, 400
        ipo = IpoModel.find_by_issuer(name)
        if not ipo:
            return {"message": "Issuer '{}' has not issued an IPO yet".format(name)}, 400

        return self.controller.forecastWrap(issuer.json(), ipo.json(issuer.name))


