from pymongo import MongoClient
from bson.json_util import dumps, loads
from .secrets import password

client = MongoClient('mongodb+srv://hooperz:' + password + '@cluster0-kkaez.mongodb.net/test?retryWrites=true&w=majority')

testUser = {
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

testBattle = {
    "battleTime": "20200515T055921.000Z",
    "brawlerId": 16000005,
    "brawlerName": "SPIKE",
    "brawlerPower": 4,
    "brawlerTrophies": 218,
    "duration": 97,
    'isStarPlayer': False,
    "mapId": 15000011,
    "mapName": "Undermine",
    "mode": "gemGrab",
    "result": "victory",
    "teams": [
        [
            {
                "brawler": {
                    "id": 16000005,
                    "name": "SPIKE",
                    "power": 4,
                    "trophies": 218
                },
                "name": "Hoo0oper",
                "tag": "#GUL2Y08J"
            },
            {
                "brawler": {
                    "id": 16000031,
                    "name": "MR. P",
                    "power": 2,
                    "trophies": 178
                },
                "name": "Brawl Power",
                "tag": "#8Y9G2YP20"
            },
            {
                "brawler": {
                    "id": 16000022,
                    "name": "TICK",
                    "power": 6,
                    "trophies": 181
                },
                "name": "secret_poepie",
                "tag": "#8P88CJ9C9"
            }
        ],
        [
            {
                "brawler": {
                    "id": 16000020,
                    "name": "FRANK",
                    "power": 1,
                    "trophies": 214
                },
                "name": "Freddy Fnafer",
                "tag": "#2LYRGQGPJ"
            },
            {
                "brawler": {
                    "id": 16000029,
                    "name": "BEA",
                    "power": 4,
                    "trophies": 124
                },
                "name": "тайный человек",
                "tag": "#9QPPP9GRL"
            },
            {
                "brawler": {
                    "id": 16000023,
                    "name": "LEON",
                    "power": 1,
                    "trophies": 263
                },
                "name": "омар",
                "tag": "#9PJLLG8CQ"
            }
        ]
    ],
    "trophyChange": 8,
    "type": "ranked"
}

testBattle2 = {
    "battleTime": "20200513T054812.000Z",
    "brawlerId": "16000020",
    "brawlerName": "FRANK",
    "brawlerPower": "1",
    "brawlerTrophies": "99",
    "duration": "NA",
    "mapId": 15000243,
    "mapName": "Cavern Churn",
    "mode": "soloShowdown",
    "players": [
        {
            "brawler": {
                "id": 16000034,
                "name": "JACKY",
                "power": 1,
                "trophies": 113
            },
            "name": "ghost_talha",
            "tag": "#80LLYL888"
        },
        {
            "brawler": {
                "id": 16000016,
                "name": "PAM",
                "power": 1,
                "trophies": 102
            },
            "name": "MASTER brawl",
            "tag": "#PQGQ9RJ2Y"
        },
        {
            "brawler": {
                "id": 16000034,
                "name": "JACKY",
                "power": 1,
                "trophies": 101
            },
            "name": "rusty",
            "tag": "#P9Y99PRUY"
        },
        {
            "brawler": {
                "id": 16000020,
                "name": "FRANK",
                "power": 1,
                "trophies": 99
            },
            "name": "Hoo0oper",
            "tag": "#GUL2Y08J"
        },
        {
            "brawler": {
                "id": 16000029,
                "name": "BEA",
                "power": 1,
                "trophies": 112
            },
            "name": "леон",
            "tag": "#8YJUV089R"
        },
        {
            "brawler": {
                "id": 16000020,
                "name": "FRANK",
                "power": 1,
                "trophies": 108
            },
            "name": "УбИтЫй_МаЛьЧиК",
            "tag": "#29YRYGPYQ"
        },
        {
            "brawler": {
                "id": 16000017,
                "name": "TARA",
                "power": 1,
                "trophies": 104
            },
            "name": "нека",
            "tag": "#9UGYY0VLG"
        },
        {
            "brawler": {
                "id": 16000026,
                "name": "BIBI",
                "power": 1,
                "trophies": 94
            },
            "name": "про",
            "tag": "#9LRY2J2LC"
        },
        {
            "brawler": {
                "id": 16000015,
                "name": "PIPER",
                "power": 1,
                "trophies": 100
            },
            "name": "[БЛЕТ] ТУЧКА",
            "tag": "#9UJUJU8PY"
        },
        {
            "brawler": {
                "id": 16000026,
                "name": "BIBI",
                "power": 1,
                "trophies": 104
            },
            "name": "Pro boxer",
            "tag": "#Y9RJ9PQ2Q"
        }
    ],
    "rank": 4,
    "trophyChange": 6,
    "type": "ranked"
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

    return foundUser

def getUserByOID(oid):
    return dumps(Users.find_one({"_id":oid}))

# Returns the object ID of the new user
def addNewUser(userData):
    new_user_id = Users.insert_one(userData).inserted_id
    return getUserByOID(new_user_id)

# Deletes all documents that match the filter
def cleanUsers(name=None, userOId=None, battleOId=None):
    userDeletionResults = Users.delete_many({"_id":userOId})
    battleDeletionResults = Battles.delete_many({"userOId": userOId})
    print("User Results deleted: " + str(userDeletionResults.deleted_count))
    print("Battle Results deleted: " + str(battleDeletionResults.deleted_count))
    return userDeletionResults.deleted_count

def insertSingleBattle(battleData):
    new_battle_id = Battles.insert_one(battleData).inserted_id
    return new_battle_id

def insertMultipleBattles(battleList):
    new_battle_ids = Battles.insert_many(battleList).inserted_ids
    return new_battle_ids

def user_test():
    addNewUser(testUser)
    getUserByTag('GUL2Y08J')
    cleanUsers(name='Hoo0oper')

def battle_test():
    addNewUser(testUser)
    foundUser = getUserByTag('GUL2Y08J')
    testBattle['userOId'] = foundUser['_id']
    testBattle2['userOId'] = foundUser['_id']
    battleList = [testBattle, testBattle2]
    insertMultipleBattles(battleList)
    cleanUsers(userOId=foundUser['_id'])
    

battle_test()