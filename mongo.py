#This file will contain the connection to the Mongo DB

#Importing files which will be used in the program
from pymongo import MongoClient

#This class will handle all of the methods that deal with the Mongo Database. 
class Database():

    def __init__(self):
        self.client = MongoClient() #Setting up the connection to mongo DB
        self.db = self.client.titanic #Creating the titanic DB
        self.db.passengers = self.db.passengers #Creating a passengers collection within the titanic DB

    #This method will add a new user to the database.
    def add(self, username, password):
        self.db.passengers.insert_one({
            "username": username,
            "password": password
        })

    #This method will see if the username and password are in the database.
    def check(self, username, password):
        user_real = self.db.passengers.find_one({
            "username": username,
            "password": password
        });
        if str(user_real) == 'None':
            flag = False
        else:
            flag = True
        return flag
