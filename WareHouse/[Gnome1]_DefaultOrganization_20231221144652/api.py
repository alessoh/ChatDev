'''
This file contains the implementation of the API endpoints for the AI HIVE web application.
'''
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Welcome to AI HIVE!"