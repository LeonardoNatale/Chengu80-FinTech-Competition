from flask_restful import Resource, reqparse
from models.investor import InvestorModel


class InvestorRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required = True,
                        help="This field cannot be blank")

    def post(self):
        data = self.parser.parse_args()

        if InvestorModel.find_by_username(data['username']):
            return {"message": "A User with that username already exists"}, 400

        user = InvestorModel(**data)
        user.save_to_db()

        return {"message": "User create successfully"}, 201