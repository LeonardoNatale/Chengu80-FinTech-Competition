from db import db
from models.investor import InvestorModel
from models.issuer import IssuerModel
from datetime import datetime as dt

class BidModel(db.Model):
    __tablename__ = 'bidz'

    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=dt.now())
    investor_id = db.Column(db.Integer, db.ForeignKey('investorz.id'), nullable=False)
    price = db.Column(db.Float(precision=3))
    amount = db.Column(db.Integer)
    issuer_id = db.Column(db.Integer, db.ForeignKey('issuerz.id'), nullable=False)

    issuer = db.relationship('IssuerModel')
    investor = db.relationship('InvestorModel')

    def __init__(self, investor, price, amount, issuer):
        self.investor_id = InvestorModel.find_by_username(investor).id
        self.price = price
        self.amount = amount
        self.issuer_id = IssuerModel.find_by_name(issuer).id

    def save_to_db(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_investor_id(cls, investor_id):
        return cls.query.filter_by(investor_id=investor_id).all()

    @classmethod
    def find_by_combination(cls, investor_id, price, amount, issuer_id):
        return cls.query.filter_by(investor_id = investor_id).filter_by(price = price).filter_by(amount=amount).filter_by(issuer_id=issuer_id).first()




