# This code is to be currently run by my local computer. 
# It will be used to automatically fetch battle records and then add them to the datebase

from app.mongo.mongoAPI import getAllUsers
from app.brawlstars.brawlstarsAPI import cleanBattleData, getPlayerBattles
from app.api import update_player_battlelog_by_tag

users = getAllUsers()

testUser = users[0]['_id']

for user in users:
    print("Trying to update {}({})".format(user['name'], user['_id']))
    res = update_player_battlelog_by_tag(user['_id'][1:])
    print(res)


