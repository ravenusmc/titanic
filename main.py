#This is the main file of the program that will actually run everything.

#import libraries which will be used in the project.
import pandas as pd
import numpy as np
from flask import Flask, session, redirect, url_for, escape, render_template, request
from pymongo import MongoClient
import bcrypt

#importing files that I have created for this project.
from data import *
from mongo import *

#Setting up flask
app = Flask(__name__)

#This function will be the login page for the app
@app.route('/', methods=['GET', 'POST'])
def login():
    #This is the object that will deal with Mongo DB.
    identity = Database()
    #If the user submits a post request this conditional statement is activated.
    if request.method == 'POST':
        #Getting the information from the form that the user submitted.
        username = request.form['username']
        password = request.form['password']
        #This method will check to ensure that the username and password are in
        #the databse.
        flag = identity.check(username, password)
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            return redirect(url_for('index'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            return redirect(url_for('sign_up'))
    return render_template('login.html', title='Login Page')

#This is the index page for the app.
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

#This function is for the sign up page where users will go to sign up to use the
#program.
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    #This is the object that will deal with Mongo DB.
    identity = Database()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #Here the identity object uses the add method to add the user to the mongo
        #databse. Once that is done, the user will be redirected to the index page.
        identity.add(username, password)
        return redirect(url_for('index'))
    return render_template('sign_up.html', title='Sign Up Page')

@app.route('/logout')
def logout():
    return render_template('sign_out.html', title='Sign Out Page')

#This code will allow the user to go to a page to look at data.
@app.route('/data')
def data():
    data = Data()
    total_passengers = data.amount_who_lived()
    return render_template('data.html', title='Data Page', total = total_passengers)

#This code will allow the user to see how many people survived by sex.
@app.route('/sex_results', methods=['POST'])
def sex_results():
    sex = str(request.form['sex'])
    data = Data()
    survived_passengers, total_passengers, lived_by_sex = data.who_lived_by_sex(sex)
    return render_template('sex_results.html', title="sex_results", total = total_passengers, sex_type = lived_by_sex, sex = sex, total_lived = survived_passengers)

#This code will display the results of how many people survived in each class.
@app.route('/class_results', methods=['POST'])
def class_results():
    class_selected = int(request.form['class'])
    data = Data()
    class_converted = data.convert_class(class_selected)
    survived_passengers, total_passengers, lived_by_class = data.who_lived_by_class(class_selected)
    return render_template('class_results.html', title="class_results", total = total_passengers, class_type = lived_by_class, class_converted = class_converted, total_lived = survived_passengers)

#This code will display the results of who survived the titanic by age.
@app.route('/age_results', methods=['POST'])
def age_results():
    age_entered = int(request.form['number'])
    data = Data()
    total_passengers, age_survived = data.age_lived(age_entered)
    return render_template('age_results.html', title="Age_results", age = age_survived, total = total_passengers, age_entered = age_entered)

@app.route('/sex_and_class_results', methods=['POST'])
def sex_and_class_results():
    sex = str(request.form['sex'])
    class_selected = int(request.form['class'])
    data = Data()
    class_converted = data.convert_class(class_selected)
    total, survived = data.survived_sex_class(sex, class_selected)
    return render_template('sex_class_results.html', title="Sex and Class Results", total = total, survived_sex_class = survived, sex = sex, class_converted = class_converted)

#This line will actually run the app.
app.run(debug=True)
