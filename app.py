from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Good morning sir"


from controller import *
