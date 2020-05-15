from flask import Flask
from .brawlstars.configs.secrets import apiKey
from .brawlstars.brawlstarsAPI import getPlayerInfo, getPlayerBattles, cleanBattleData
from .mongo.mongoAPI import getUserByTag, addNewUser
from bson.json_util import dumps
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
        return dumps(addNewUser(newPlayer))
    else:
        return foundUser




