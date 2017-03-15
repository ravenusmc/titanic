
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

#Setting up flask
app = Flask(__name__)

#This code will send the user to the index/home page
@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

#This code will allow the user to go to a page to look at data.
@app.route('/data')
def data():
    return render_template('data.html', title='Data Page')

#This line will actually run the app.
app.run(debug=True)
