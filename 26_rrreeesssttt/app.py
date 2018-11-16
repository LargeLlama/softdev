from flask import Flask, render_template
import urllib, json
from util import words

app = Flask(__name__)

@app.route("/")
def home():
    temp = words.get_definition('lacrosse')
    return render_template("home.html", definition = temp)
