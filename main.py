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
    if request.method == 'POST':
        my_server = Database()
        session['username'] = request.form['username']
        session['firstname'] = request.form['firstname']
        return redirect(url_for('index'))
    return render_template('login.html', title='Login Page')

#     coll = my_server.database_setup()
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     user_name = request.form['user_name']
#     password = request.form['password']
#     coll.insert_one({"first_name": first_name, "last_name": last_name, "user_name": user_name, "password": password})
#     return render_template('test_login.html', title='Home Page')

#This is the index page for the app.
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', title='Home Page')
        # return 'Logged in as %s' % escape(session['username', 'firstname'])
    return 'You are not logged in'

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
    total, survived = data.age_lived(sex, class_selected)
    return render_template('sex_class_results.html', title="Sex and Class Results", total = total, survived_sex_class = survived, sex = sex, class_converted = class_converted)

# set the secret key.
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#This line will actually run the app.
app.run(debug=True)



###### OLD CODE

#This code will send the user to the index/home page
# @app.route('/test', methods=['POST'])
# def login_t():
#     my_server = Database()
#     coll = my_server.database_setup()
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     user_name = request.form['user_name']
#     password = request.form['password']
#     # password = b"password"
#     # hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
#     coll.insert_one({"first_name": first_name, "last_name": last_name, "user_name": user_name, "password": password})
#     return render_template('test_login.html', title='Home Page')

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Login Page')
#
# @app.route('/index')
# def index():
#     if 'username' in session:
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'
    # return render_template('index.html', title='Home Page')
