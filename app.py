import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
from auth import AuthError, requires_auth


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  return app

app = create_app()

@app.route('/')
def healthy_check():
  return jsonify({
    'healthy': 'check'
  })

@app.route('/actors')
@requires_auth('get:actors')
def get_actors(payload):
  actors_query = Actors.query.all()

  if actors_query is None:
    abort(404)

  actors = [actor.format() for actor in actors_query]

  return jsonify({
    'actors': actors
  })

@app.route('/actors', methods=['POST'])
@requires_auth('create:actor')
def create_actor():
  
  body = request.get_json()

  new_actor = Actors(
    name=body.get('name', ''),
    age=body.get('age', ''),
    gender=body.get('gender', '')
  )

  new_actor.insert()

  return jsonify({
    'status': 'succesful'
  })

@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(payload, id):
  
  actor = Actors.query.filter(Actors.id==id).one_or_none()
  actor.delete()


  return jsonify({
    'status': 'succesful'
  })

@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actor')
def edit_actor(payload, id):
  
  actor = Actors.query.filter(Actors.id==id).one_or_none()
  body = request.get_json()

  actor.name = body.get('name', '')
  actor.age = body.get('age', '')
  actor.gender = body.get('gender', '')

  actor.update()

  return jsonify({
    'status': 'succesful'
  })

@app.route('/movies')
@requires_auth('get:movies')
def get_movies():
  movies_query = Movies.query.all()

  if movies_query is None:
    abort(404)

  movies = [movie.format() for movie in movies_query]

  return jsonify({
    'movies': movies
  })

@app.route('/movies', methods=['POST'])
@requires_auth('create:movie')
def create_movie():
  
  body = request.get_json()

  new_movie = Movies(
    title=body.get('title', ''),
    release_date=body.get('release_date', '')
  )

  new_movie.insert()

  return jsonify({
    'status': 'succesful'
  })

@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(id):
  
  movie = Movies.query.filter(Movies.id==id).one_or_none()
  movie.delete()

  return jsonify({
    'status': 'succesful'
  })

@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movie')
def edit_movie(id):
  
  movie = Movies.query.filter(Movies.id==id).one_or_none()
  body = request.get_json()

  movie.title = body.get('title', '')
  movie.release_date = body.get('release_date', '')

  movie.update()

  return jsonify({
    'status': 'succesful'
  })

if __name__ == '__main__':
    app.run()