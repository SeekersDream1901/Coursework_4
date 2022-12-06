from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genres import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        data = {
            "page": request.args.get('page')
        }
        genres = genre_service.get_all(data)
        return genres_schema.dump(genres), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)

        return "", 201


@genres_ns.route('/<int:git>')
class GenreView(Resource):
    def get(self, git: int):
        genre = genre_service.get_one(git)

        return genre_schema.dump(genre), 200

    def put(self, git: int):
        req_json = request.json
        req_json['id'] = git

        genre_service.update(git)

        return "", 204

    def delete(self, gid: int):
        genre_service.delete(gid)

        return "", 204
