from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movies import MovieSchema

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = {
            "year": request.args.get('year'),
            "director_id": request.args.get('director_id'),
            "genre_id": request.args.get('genre_id'),
            "page": request.args.get('page'),
            "status": request.args.get('status')
        }
        movies = movie_service.get_all(data)
        response = movies_schema.dump(movies)

        return response

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "Фильм создан", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        response = movie_schema.dump(movie)

        return response, 200

    def put(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return "", 204
