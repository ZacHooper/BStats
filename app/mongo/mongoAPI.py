from pymongo import MongoClient
from bson.json_util import dumps, loads
from .secrets import password

client = MongoClient('mongodb+srv://hooperz:' + password + '@cluster0-kkaez.mongodb.net/test?retryWrites=true&w=majority')

user = {
    "3vs3Victories": 1947,
    "bestRoboRumbleTime": 0,
    "bestTimeAsBigBrawler": 0,
    "brawlers": [
        {
            "gadgets": [ ],
            "highestTrophies": 571,
            "id": 16000000,
            "name": "SHELLY",
            "power": 8,
            "rank": 21,
            "starPowers": [ ],
            "trophies": 514
        },
        {
            "gadgets": [],
            "highestTrophies": 561,
            "id": 16000001,
            "name": "COLT",
            "power": 8,
            "rank": 21,
            "starPowers": [ ],
            "trophies": 525
        },
        {
            "gadgets": [ ],
            "highestTrophies": 556,
            "id": 16000002,
            "name": "BULL",
            "power": 8,
            "rank": 21,
            "starPowers": [ ],
            "trophies": 519
        },
    ],
    "club": { },
    "duoVictories": 31,
    "expLevel": 79,
    "expPoints": 33409,
    "highestTrophies": 13322,
    "isQualifiedFromChampionshipChallenge": False,
    "name": "Hoo0oper",
    "nameColor": "0xfff05637",
    "soloVictories": 112,
    "tag": "#GUL2Y08J",
    "trophies": 13319
}

db = client.Brawlstars

Users = db.get_collection('Users')
Battles = db.get_collection('Battles')

# Returns the full user object as a JSON object
def getUserByTag(playerTag):
    #Check if playerTag already has a '#' if not add it
    if '#' not in playerTag:
        playerTag = '#' + playerTag

    foundUser = Users.find_one({"tag": playerTag})

    return foundUser if foundUser is None else dumps(foundUser)

# Returns the object ID of the new user
def addNewUser(userData):
    new_user_id = Users.insert_one(user).inserted_id
    print("New User added with ID: " + str(new_user_id))
    return new_user_id

# Deletes all documents that match the filter
def cleanUsers(name=None):
    deletionResults = Users.delete_many({"name":name}) 
    print("Results deleted: " + str(deletionResults.deleted_count))
    return deletionResults.deleted_count

def test():
    addNewUser(user)
    getUserByTag('GUL2Y08J')
    cleanUsers(name='Hoo0oper')