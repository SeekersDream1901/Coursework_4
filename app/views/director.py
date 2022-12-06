from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.directors import DirectorSchema
from app.container import director_service

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        data = {
            "page": request.args.get('page')
        }
        directors = director_service.get_all(data)

        return directors_schema.dump(directors), 201

    def post(self):
        req_json = request.json
        director_service.create(req_json)

        return "", 201


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)

        return director_schema.dump(director), 201

    def put(self, did: int):
        req_json = request.json
        req_json['id'] = did

        director_service.update(req_json)

        return "", 204

    def delete(self, did: int):
        director_service.delete(did)

        return "", 204
