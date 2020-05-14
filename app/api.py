from flask import Flask
from .brawlstars.configs.secrets import apiKey
from .brawlstars.brawlstarsAPI import getPlayerInfo, getPlayerBattles, cleanBattleData
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




