#This is the main file of the program that will actually run everything.

#import libraries which will be used in the project.
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

#importing files that I have created for this project.
from data import *

#Setting up flask
app = Flask(__name__)

#This code will send the user to the index/home page
@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

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
    return render_template('age_results.html', title="Age_results", age = age_survived, total = total_passengers)

#This line will actually run the app.
app.run(debug=True)
