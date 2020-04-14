# Captone

#### 

# Host URL

The API is hosted on https://rory-dwan-capstone.herokuapp.com/

# Auth0 login URL

https://dev-jlpcmeif.eu.auth0.com/authorize?response_type=token&audience=Capstone&client_id=47XrFFygWI9vsG1OwET2Vw5VssoX3ARE&redirect_uri=https://rory-dwan-capstone.herokuapp.com

# Auth0 logout URL

https://dev-jlpcmeif.eu.auth0.com/v2/logout?client_id=47XrFFygWI9vsG1OwET2Vw5VssoX3ARE&returnTo=https://rory-dwan-capstone.herokuapp.com

# Login Details for Auth0

# Casting Assistant
Username: castingassistant@udacity.ie
Password: CastingAssistant20

# Casting Director
Username: castingdirector@udacity.ie
Password: CastingDirector20

# Executive Producer
Username: executiveproducer@udacity.ie
Password: ExecutiveProducer20

# Endpoints

GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
DELETE '/actors/<int:id>'
DELETE '/movies/<int:id>'
PATCH '/actors/<int:id>'
PATCH '/movies/<int:id>'

GET '/actors'
- Fetches all the actors in the database
- Request Arguments: None
- Returns: An object with a two keys, the first is 'actors', which contains all the actors in the database.
- the second is 'status', which indicates that the request was successful.

{
    'actors': [],
    'status' : "successful"
}

GET '/movies'
- Fetches all the movies in the database
- Request Arguments: None
- Returns: An object with a two keys, the first is 'movies', which contains all the movies in the database.
- the second is 'status', which indicates that the request was successful.

{
    'movies': [],
    'status' : "successful"
}

POST '/acotrs'
- Creates a new actor entry in the database
- Request Arguments: {
    'name':
    'age':
    'gender'
}
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}

POST '/movies'
- Creates a new movie entry in the database
- Request Arguments: {
    'title': 
    'release_date': 
}
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}

DELETE '/actors/<int:id>'
- Deletes an actor from the database
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}

DELETE '/movies/<int:id>'
- Deletes a movie from the database
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}

PATCH '/acotrs/<int:id>'
- Edits an actor entry in the database
- Request Arguments: {
    'name':
    'age':
    'gender'
}
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}

PATCH '/movies/<int:id>'
- Edits a movie entry in the database
- Request Arguments: {
    'title':
    'release_date':
}
- Returns: An object with single key, 'status', which indicates that the request was successful.

{
    'status' : "successful"
}
