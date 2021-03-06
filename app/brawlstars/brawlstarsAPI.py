#from app.brawlstars.configs.secrets import apiKey
from .configs.secrets import apiKey # devlopment
import requests
import pandas as pd
import os
proxyDict = {
              "http"  : os.environ.get('FIXIE_URL', ''),
              "https" : os.environ.get('FIXIE_URL', '')
            }

url = 'https://api.brawlstars.com/v1/'


def getPlayerInfo(playerTag):
    payload = {"authorization": "Bearer " + apiKey}

    endpoint = url + 'players/%23' + playerTag
    print(endpoint)

    res = requests.get(endpoint, params=payload, proxies=proxyDict)
    json = res.json()

    return json

def getPlayerBattles(playerTag):
    payload = {"authorization": "Bearer " + apiKey}
    
    if '#' in playerTag:
        endpoint = url + 'players/' + playerTag[1:] + '/battlelog'
    else:
        endpoint = url + 'players/%23' + playerTag + '/battlelog'

    res = requests.get(endpoint, params=payload, proxies=proxyDict)
    print(res)
    jsonised = res.json()

    return jsonised

# Requires a list of battles (hint: use getPlayerBattles) and a user's play tag. 
# Will return a json list of battles cleaned up to make more sense in the database.
def cleanBattleData(battleList, playerTag):
        
    cleanBattles = []

    for battles in battleList['items']:
        battle = battles['battle']
        
        
        # Default Values
        cleanBattle = {
            "_id":battles['battleTime'],
            "duration": battle['duration'] if 'duration' in battle else 'NA',
            "mode":battle['mode'],
            "trophyChange":battle['trophyChange'] if 'trophyChange' in battle else 'NA',
            "type":battle['type'] if 'type' in battle else 'NA',
            "mapId":battles['event']['id'],
            "mapName":battles['event']['map']
        }

        # Results / Ranks
        if 'result' in battle:
            cleanBattle['result'] = battle['result']
        elif 'rank' in battle:
            cleanBattle['rank'] = battle['rank']

        # Star Player
        if 'starPlayer' in battle:
            cleanBattle['isStarPlayer'] = True if battle['starPlayer']['tag'] == ('#' + playerTag) else False

        # Add in Boss Fight Level    
        if battle['mode'] == 'bossFight':
            cleanBattle['levelName'] = battle['level']['name']
            cleanBattle['levelId'] = battle['level']['id']

        # Play Brawler Details init
        brawlerData = {}

        # Create an object containing the user's brawler details
        def getBrawlerDetails (players):
            for player in players:
                    if player['tag'] == ('#' + playerTag):
                        # Handle Friendly Matches
                        if 'type' not in battle:
                            return {
                                "brawlerId": player['brawler']['id'],
                                "brawlerName": player['brawler']['name'],
                                "brawlerPower": player['brawler']['power'],
                                "brawlerTrophies": player['brawler']['trophies']
                            }
                        elif battle['type'] is 'ranked':
                            return {
                                "brawlerId": player['brawler']['id'],
                                "brawlerName": player['brawler']['name'],
                                "brawlerPower": player['brawler']['power'],
                                "brawlerTrophies": player['brawler']['trophies']
                            }
                        else:
                            return {
                                "brawlerId": player['brawler']['id'],
                                "brawlerName": player['brawler']['name']
                            }

        # Team Specifc flow - gemgrab, duo showdown, etc
        if 'teams' in battle:        
            cleanBattle['teams'] = battle['teams']
            for team in battle['teams']:
                data = getBrawlerDetails(team)
                if data is not None:
                    brawlerData.update(data)
        
        # Player specific flow - solo showdown, robo rumble, etc
        if 'players' in battle:
            cleanBattle['players'] = battle['players']
            data = getBrawlerDetails(battle['players'])
            if data is not None:
                brawlerData.update(data)

        # Add the user's brawler data to the clean battle dict
        cleanBattle.update(brawlerData)

        # Add the dict to the list of clean battles 
        cleanBattles.append(cleanBattle)
    
    return {"battles": cleanBattles}

