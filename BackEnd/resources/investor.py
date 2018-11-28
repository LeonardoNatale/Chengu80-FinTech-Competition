from flask_restful import Resource, reqparse
from models.investor import InvestorModel


class InvestorRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        data = self.parser.parse_args()

        print(data)
        if InvestorModel.find_by_username(data['username']):
            return {"message": "A User with that username already exists"}, 400

        user = InvestorModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201


class InvestorLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        data = self.parser.parse_args()

        user = InvestorModel.find_by_username(data['username'])

        if not user:
            return {"message": "Invalid Username"}, 400

        if user.password != data['password']:
            return {"message": "Invalid Password"}, 401

        return {"message": "Login Successful"}, 200
