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
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('avg_credit_card_spending_semi_annual',
                        type=int,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        data = self.parser.parse_args()

        user = IssuerModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201