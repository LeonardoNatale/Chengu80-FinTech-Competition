from db import db
from models.holding import HoldingModel
from models.prices import PriceModel

class IssuerModel(db.Model):
    __tablename__ = 'issuerz'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    marital_status = db.Column(db.Integer)
    sex = db.Column(db.Integer())
    number_of_kids = db.Column(db.Integer)
    occupation = db.Column(db.Integer)
    education_level = db.Column(db.Integer)
    house_tenure = db.Column(db.Integer)
    income_past12months = db.Column(db.Float(precision=2))
    intended_education = db.Column(db.Integer)
    graduation_year = db.Column(db.Integer)
    intended_occupation = db.Column(db.Integer)

    ipo = db.relationship('IpoModel', backref='ipoz', uselist='False')
    bid = db.relationship('BidModel')
    holding = db.relationship(HoldingModel)
    prices = db.relationship(PriceModel)

    def __init__(self, name, age, marital_status, sex, number_of_kids, occupation, education_level, house_tenure,
                 income_past12months, intended_education, graduation_year, intended_occupation):
        self.name = name
        self.age = age
        self.marital_status = marital_status
        self.sex = sex
        self.number_of_kids = number_of_kids
        self.occupation = occupation
        self.education_level = education_level
        self.house_tenure = house_tenure
        self.income_past12months = income_past12months
        self.intended_education = intended_education
        self.graduation_year = graduation_year
        self.intended_occupation = intended_occupation

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'name': self.name,
                'age': self.age,
                'marital_status': self.marital_status,
                'sex': self.sex,
                'number_of_kids': self.number_of_kids,
                'occupation': self.occupation,
                'education_level': self.education_level,
                'house_tenure': self.house_tenure,
                'income_past12months': self.income_past12months,
                'intended_education': self.intended_education,
                'graduation_year': self.graduation_year,
                'intended_occupation': self.intended_occupation}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

