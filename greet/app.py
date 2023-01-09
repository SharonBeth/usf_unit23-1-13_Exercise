"""First Server exercise-Unit 23-1-11"""
# 
# from flask import Flask, request

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"


@app.route('/welcome/back')
def welcome_back():
    return "welcome back"