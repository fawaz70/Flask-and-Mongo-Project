from fastapi import FastAPI  # Imports Flask within this as well
# Mongo used as our database
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017/')

# Documentation on root
app = FastAPI(docs_url="/")

# Connect to our database as well as create index's for easy querying
try:
    connection = client.get_database('logs').get_collection("user_logs")
    connection.create_index('userId')
    connection.create_index('actions.time')
    connection.create_index('actions.type')
except ConnectionError as error:
    print('Error: ' + str(error) + '! Could not connect to server')


# Our POST method which stores the json file given to use from the front end
@app.post("/store", status_code=201)
def take_json(body: dict):
    response_body = {
        "message": "JSON received!",
        "sender": body.get("userId")
    }
    try:
        connection.insert_one(body)
    except ConnectionError as error:
        print('Error: ' + str(error) + '! Could not insert')
    return response_body


# This is the GET method which is used to get our query results based on the set of inputs provided
@app.get("/retrieve", status_code=200)
def get_log(uId: str = None, action_type: str = None, date_from: str = None, date_to: str = None):
    query = {}  # Set our query to nothing which will return everything if no arguments provided
    if date_from or date_to:
        query['actions.time'] = {}  # If one of the dates exist in the arguments then set up time for query
    if uId:
        query['userId'] = uId
    if action_type:
        query['actions.type'] = {'$in': action_type.split(',')}  # This allows multiple types separated by commas
    # {"actions.time":{$gte:"2018-10-18T21:37:30-06:00"}}
    # These 2 if statements add the 2 arguments to time for querying
    if date_from:
        query['actions.time']['$gte'] = date_from
    if date_to:
        query['actions.time']['$lte'] = date_to
    try:
        data = list(connection.find(query, {'_id': 0}))
    except ConnectionError as error:
        print('Error: ' + str(error) + '! Could not query on server')
    return {'data': data}
