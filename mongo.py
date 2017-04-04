#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient

class Database():

    def database_setup(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        db = self.client.titanic #Creating the titanic DB
        coll = db.users #Creating a users collection within the titanic DB
        # db.users.insert_one({
        #   "first_name": "Test",
        #   "last_name": "Me",
        #   "user": "TestMe",
        #   "password": "pass"
        # )}
        return coll

# client = MongoClient()
# db = client.titanic
# db.users
# db.users.insert_one({
#     "first_name": "Test",
#     "last_name": "Me",
#     "user": "TestMe",
#     "password": "pass"

# })
