from flask import Flask
from .brawlstars.configs.secrets import apiKey
from .brawlstars.brawlstarsAPI import getPlayerInfo, getPlayerBattles, cleanBattleData
from .mongo.mongoAPI import getUserByTag, addNewUser, insertMultipleBattles
from bson.json_util import dumps, loads
import requests

app = Flask(__name__)

@app.route('/')
def get_current_time():
    return {'time': apiKey}

@app.route('/player/info/<playerTag>')
def get_player_info(playerTag):
    return getPlayerInfo(playerTag)

@app.route('/player/battles/<playerTag>')
def get_player_battles(playerTag):
    return cleanBattleData(getPlayerBattles(playerTag), playerTag)

@app.route('/api/v1/player/info/<playerTag>')
def get_player_info_from_db(playerTag):
    return getUserByTag(playerTag)

@app.route('/api/v1/player/new/<playerTag>')
def add_new_player(playerTag):
    foundUser = getUserByTag(playerTag)
    if foundUser is None:
        newPlayer = getPlayerInfo(playerTag)
        newPlayer['_id'] = newPlayer.pop('tag')
        return addNewUser(newPlayer)
    else:
        return dumps(foundUser)

@app.route('/api/v1/battle/update/tag/<playerTag>')
def update_player_battlelog_by_tag(playerTag):
    # Get the user
    foundUser = getUserByTag(playerTag)
    UserOID = foundUser['_id']

    # Get the User's battlelog
    battleList = getPlayerBattles(playerTag)

    #Clean the data
    cleanBattleList = cleanBattleData(battleList, playerTag)

    #Add the userOID to every battle records
    for battle in cleanBattleList['battles']:
        battle['userOID'] = UserOID
    
    # Add the battlelist to the db
    return dumps(insertMultipleBattles(cleanBattleList['battles']))


