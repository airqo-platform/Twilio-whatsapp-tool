import pymongo
from pymongo import MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["airqommunity_whatsapp"]
mycol = mydb["ccontactdetails"]
mycol2 = mydb["message_log"]

#mydb.contactdetails.drop()
#mydb.message_log.drop()