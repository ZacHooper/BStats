from pymongo import MongoClient
from secrets import getPassword

client = MongoClient('mongodb+srv://hooperz:' + getPassword() + '@cluster0-kkaez.mongodb.net/test?retryWrites=true&w=majority')

db = client.Brawlstars

