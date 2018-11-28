from db import db
from models.issuer import IssuerModel


class IpoModel(db.Model):
    __tablename__ = 'ipoz'

    id = db.Column(db.Integer, primary_key=True)
    credit_card_percentage = db.Column(db.Float(precision=2))
    shares_offering = db.Column(db.Integer)
    market_lot = db.Column(db.Integer)
    minimum_order = db.Column(db.Integer)
    suggested_price = db.Column(db.Integer)
    minimum_price = db.Column(db.Integer)
    call_option = db.Column(db.Integer)
    put_option = db.Column(db.Integer)
    date = db.Column(db.String(10))

    issuer_id = db.Column(db.Integer, db.ForeignKey('issuerz.id'), nullable=False)
    issuer = db.relationship('IssuerModel')

    def __init__(self, issuer_name, credit_card_percentage, shares_offering, market_lot, minimum_order, call_option, put_option, date):
        self.issuer_id = IssuerModel.find_by_name(issuer_name).id
        self.credit_card_percentage = credit_card_percentage
        self.shares_offering = shares_offering
        self.market_lot = market_lot
        self.minimum_order = minimum_order
        self.call_option = call_option
        self.put_option = put_option
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self, name):
        return {'issuer_name': name,
                'credit_card_percentage': self.credit_card_percentage,
                'shares_offering': self.shares_offering,
                'market_lot': self.market_lot,
                'minimum_order': self.minimum_order,
                'call_option': self.call_option,
                'put_option': self.put_option,
                'date': self.date}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_issuer(cls, issuer):
        try:
            issuer_id = IssuerModel.find_by_name(issuer).id
            return cls.query.filter_by(issuer_id=issuer_id).first()
        except:
            return None

    @classmethod
    def find_all(cls):
        try:
            return cls.query.all()
        except:
            return None

