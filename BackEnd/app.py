from flask import Flask
from flask_restful import Api

from resources.issuer import IssuerRegister
from resources.investor import InvestorRegister, InvestorLogin
from resources.ipo import Ipo, Ipos
from resources.bid import Bid, Bids
from resources.holding import Holdings
from resources.suggested_price import SuggestedPrice
from resources.prices import Price
from resources.execute import Execute
from flask_cors import CORS



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://group2:123456@10.240.61.106:5432/group2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(IssuerRegister, '/<name>/issuer')
api.add_resource(InvestorRegister, '/register/investor')
api.add_resource(InvestorLogin, '/login/investor')
api.add_resource(Ipo, '/<string:name>/ipo')
api.add_resource(Ipos, '/ipos')
api.add_resource(Bid, '/<investor>/bid')
api.add_resource(Bids, '/<string:investor>/bids')
api.add_resource(Holdings, '/<string:investor>/holdings')
api.add_resource(SuggestedPrice, '/<string:name>/suggested_price')
api.add_resource(Price, '/<string:name>/prices')
api.add_resource(Execute, '/<string:name>/execute')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)



