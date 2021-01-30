from flask import jsonify
from flask_restful import Resource

from app.model import Proof_Model
from app.utils import post_proof


class Proof(Resource):
    def get(self):
        return jsonify(Proof_Model.query.all())

    def post(self):
        return post_proof()
