import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9yeHdCOFYybUFDY01zckZsd1g3bCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qbHBjbWVpZi5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDA4NzYxMTI5OTYzNjc4MDI4MDciLCJhdWQiOlsiQ2Fwc3RvbmUiLCJodHRwczovL2Rldi1qbHBjbWVpZi5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg2NzA0NDQ5LCJleHAiOjE1ODY3MTE2NDksImF6cCI6IjQ3WHJGRnlnV0k5dnNHMU93RVQyVnc1VnNzb1gzQVJFIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSJdfQ.Pt5zNuVSXg0Qu4IS5Ks-7oca_6qllTbjOmXxh7Do87ePE5b4eeRgySGXL7r6O7W46fQKVe0c2jnFre5fmVYu_HxQugD8n2OHJL2ElomZFSE7Pk5ExP02mkRWr1eyIRAmgM1weKnUIa3Ga_cHS7n9Irhyl7qRqkZmQPsBaL3NGrZw41N3FkGDvrTMy3ql_tol4fdNMXBgaEJs5tB1m3m1bawJLd4FvUCMN5zWMZNBz5Z5dvtxAkK5aMKtJ3oOrpBXUnDCieR-ZCNprSwU1m6EsEP_8WZMl9BVdHkugWhdqzHnwblu2w7a1jkaUfLmYQ7vEMZQ6Tv-FwftS_AeAVNrKQ'
expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im9yeHdCOFYybUFDY01zckZsd1g3bCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qbHBjbWVpZi5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDA4NzYxMTI5OTYzNjc4MDI4MDciLCJhdWQiOlsiQ2Fwc3RvbmUiLCJodHRwczovL2Rldi1qbHBjbWVpZi5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg2NzA0NDQ5LCJleHAiOjE1ODY3MTE2NDksImF6cCI6IjQ3WHJGRnlnV0k5dnNHMU93RVQyVnc1VnNzb1gzQVJFIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvciIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSJdfQ.Pt5zNuVSXg0Qu4IS5Ks-7oca_6qllTbjOmXxh7Do87ePE5b4eeRgySGXL7r6O7W46fQKVe0c2jnFre5fmVYu_HxQugD8n2OHJL2ElomZFSE7Pk5ExP02mkRWr1eyIRAmgM1weKnUIa3Ga_cHS7n9Irhyl7qRqkZmQPsBaL3NGrZw41N3FkGDvrTMy3ql_tol4fdNMXBgaEJs5tB1m3m1bawJLd4FvUCMN5zWMZNBz5Z5dvtxAkK5aMKtJ3oOrpBXUnDCieR-ZCNprSwU1m6EsEP_8WZMl9BVdHkugWhdqzHnwblu2w7a1jkaUfLmYQ7vEMZQ6Tv-FwftS_AeAVNrKQ'
permissions_not_included_token = 

expired_header = 'Bearer' + ' ' + expired_token
permission_not_found = 'Bearer' + 
header = 'Bearer' + ' ' + token

expired_auth_header = {
  'Authorization': expired_header
}
auth_header = {
  'Authorization': header
}

class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".\
            format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer', 'Token': token}

        self.actor = Actors(
            name= 'Buzz',
            age= '21',
            gender= 'male'
        )

        self.movie = Movies(
            title='Hardy Bucks',
            release_date='21st'
        )

        self.new_actor = {
            'name': 'French Toast',
            'age': '28',
            'gender': 'Male'
        }

        self.new_movie = {
            'title': 'French Toast',
            'release_date': '28'
        }

        self.edit_actor = {
            'name': 'Eddie',
            'age': '23',
            'gender': 'Female'
        }

        self.edit_movie = {
            'title': 'Hardy Bucks 2',
            'release_date': '22nd'
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.actor.insert()
        self.movie.insert()


    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        response = self.client().get('/actors', headers=auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_create_actor(self):
        response = self.client().post('/actors', headers=auth_header, json=self.new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'successful')

    def test_delete_actor(self):
        response = self.client().delete('/actors/20', headers=auth_header)
        data = json.loads(response.data)

        actor = Actors.query.filter(Actors.id==3).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(actor, None)

    def test_edit_actor(self):
        response = self.client().patch('/actors/4', headers=auth_header, json=self.edit_actor)
        data = json.loads(response.data)

        actor = Actors.query.filter(Actors.id==1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'successful')
        self.assertEqual(actor.name, 'Eddie')

    def test_get_movies(self):
        response = self.client().get('/movies', headers=auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_create_movie(self):
        response = self.client().post('/movies', headers=auth_header, json=self.new_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'successful')

    def test_delete_movie(self):
        response = self.client().delete('/movies/20', headers=auth_header)
        data = json.loads(response.data)

        movie = Movies.query.filter(Movies.id==2).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(movie, None)

    def test_edit_movie(self):
        response = self.client().patch('/movies/4', headers=auth_header, json=self.edit_movie)
        data = json.loads(response.data)

        movie = Movies.query.filter(Movies.id==4).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'successful')
        self.assertEqual(movie.title, 'Hardy Bucks 2')

    def test_405_create_actor_method_not_allowed(self):
        response = self.client().post('/actors/1000', headers=auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(data['status'], 'method not allowed')

    def test_404_delete_actor_doesnt_exist(self):
        response = self.client().delete('/actors/1000', headers=auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'not found')
 

    def test_404_delete_movie_doesnt_exist(self):
        response = self.client().delete('/movies/1000', headers=auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'not found')

    def test_404_edit_actor_doesnt_exist(self):
        response = self.client().patch('/actors/1000', headers=auth_header, json=self.edit_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'not found')

    def test_404_edit_movie_doesnt_exist(self):
        response = self.client().patch('/movies/1000', headers=auth_header, json=self.edit_movie)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'not found')
    
    def test_401_unauthorised(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['status'], 'unauthorised')
    
    def test_403_permission_not_found(self):
        response = self.client().get('/actors', headers=expired_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(data['status'], 'unauthorised')
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()