from flask_restful import Resource, reqparse
from models.issuer import IssuerModel


class IssuerRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('age',
                        type = int,
                        required = True,
                        help="This field cannot be blank")

    parser.add_argument('marital_status',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('sex',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('number_of_kids',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('occupation',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('education_level',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('house_tenure',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('income_past12months',
                        type=float,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('intended_education',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('graduation_year',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('intended_occupation',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    def post(self, name):
        if IssuerModel.find_by_name(name):
            return {"message": "An issuer with this name already exists"}, 400
        data = self.parser.parse_args()
        user = IssuerModel(name, **data)
        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return {"message": "User created successfully"}, 201

    def get(self, name):
        issuer = IssuerModel.find_by_name(name)
        if issuer:
            return issuer.json()
        return {"message": "User does not exist"}, 400

    def delete(self, name):
        issuer = IssuerModel.find_by_name(name)
        if issuer:
            issuer.delete_from_db()
            return {"message": "issuer deleted"}
        return {"message": "User does not exist"}, 404
