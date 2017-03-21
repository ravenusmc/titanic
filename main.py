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

@app.route('/sex_results', methods=['POST'])
def sex_results():
    sex = str(request.form['sex'])
    data = Data()
    total_passengers, lived_by_sex = data.who_lived_by_sex(sex)
    return render_template('sex_results.html', title="sex_results", total = total_passengers, sex_type = lived_by_sex, sex = sex)


#This line will actually run the app.
app.run(debug=True)
