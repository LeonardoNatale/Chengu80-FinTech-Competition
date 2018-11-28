from db import db


class HoldingModel(db.Model):
    __tablename__ = 'holdingz'

    id = db.Column(db.Integer, primary_key=True)
    investor_id = db.Column(db.Integer, db.ForeignKey('investorz.id'), nullable=False)
    price = db.Column(db.Float(precision=3))
    amount = db.Column(db.Integer)
    issuer_id = db.Column(db.Integer, db.ForeignKey('issuerz.id'), nullable=False)

    issuer = db.relationship('IssuerModel')
    investor = db.relationship('InvestorModel')

    def __init__(self, investor_id, price, amount, issuer_id):
        self.investor_id = investor_id
        self.price = price
        self.amount = amount
        self.issuer_id = issuer_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_investor_id(cls, _id):
        return cls.query.filter_by(investor_id=_id).all()




