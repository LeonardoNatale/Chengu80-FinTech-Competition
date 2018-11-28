from db import db

class PriceModel(db.Model):
    __tablename__ = 'pricez'

    id = db.Column(db.Integer, primary_key=True)
    suggested_price = db.Column(db.Float(precision=3))
    minimum_price = db.Column(db.Float(precision=3))
    call_price = db.Column(db.Float(precision=3))
    put_price = db.Column(db.Float(precision=3))
    issuer_id = db.Column(db.Integer, db.ForeignKey('issuerz.id'), nullable=False)

    issuer = db.relationship('IssuerModel')

    def __init__(self, issuer_id, suggested_price, minimum_price, call_price, put_price):
        self.issuer_id = issuer_id
        self.suggested_price = suggested_price
        self.minimum_price = minimum_price
        self.call_price = call_price
        self.put_price = put_price

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"suggested_price": self.suggested_price, "callable_price": self.call_price, "put_price": self.put_price}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_issuer_id(cls, _id):
        return cls.query.filter_by(issuer_id=_id).first()




