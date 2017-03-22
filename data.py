#This file will hold the class that will manipulate the data on the titanic.


#Importing files that will be used for the project
import pandas as pd
import numpy as np

class Data():

    #The following method will show the user the total amount of people on the
    #Titanic.
    def amount_who_lived(self):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        return total_passengers

    #This method will show the user who survived the sinking of the titanic by
    #sex.
    def who_lived_by_sex(self, sex):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        sex_type = len(self.__data[(self.__data.Sex == sex) & (self.__data.Survived == 1)])
        return total_passengers, sex_type

    #This method will show the user who survived the sinking of the titanic by
    #class.
    def who_lived_by_class(self, class_type):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        class_type = len(self.__data[(self.__data.Pclass == class_type) & (self.__data.Survived == 1)])
        return total_passengers, class_type



# data = Data()
# data.who_lived_by_sex('male')
