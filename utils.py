from flask import Flask
from flask_restful import Api

from app.action import Proof
from app.model import Base, engine


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SQLACHEMY_TRACK_MODIFICATIONS']=False
    # db.init_app(app)
    app.app_context().push()

    _resources(api)
    _init_db()

    return app


def _resources(api):
    api.add_resource(Proof, '/proof/')


def _init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
