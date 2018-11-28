from db import db


class IssuerModel(db.Model):
    __tablename__ = 'issuers'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    marital_status = db.Column(db.Integer)
    sex = db.Column(db.Integer())
    number_of_kids = db.Column(db.Integer)
    occupation = db.Column(db.Integer)
    education_level = db.Column(db.Integer)
    house_tenure = db.Column(db.Integer)
    income_past12months = db.Column(db.Float(precision = 2))
    avg_credit_card_spending_semi_annual = db.Column(db.Float(precision = 2))

    def __init__(self, age, marital_status, sex, number_of_kids, occupation, education_level, house_tenure, income_past12months, avg_credit_card_spending_semi_annual):
        self.age = age
        self.marital_status = marital_status
        self.sex = sex
        self.number_of_kids = number_of_kids
        self.occupation = occupation
        self.education_level = education_level
        self.house_tenure = house_tenure
        self.income_past12months = income_past12months
        self.avg_credit_card_spending_semi_annual = avg_credit_card_spending_semi_annual

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_name(cls,name):
        cls.query.filter_by(id=name).first()

