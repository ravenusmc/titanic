#This file will hold the class that will manipulate the data on the titanic.


#Importing files that will be used for the project
import pandas as pd
import numpy as np

class Data():

    #The following method
    def amount_who_lived(self):
        self.__data = pd.read_csv('train.csv')

data = Data()
data.amount_who_lived()
