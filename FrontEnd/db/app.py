from flask import Flask
from flask_restful import Api

from resources.issuer import IssuerRegister


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://group2:123456@10.240.61.106:5432/group2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(IssuerRegister, '/register/issuer')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)





