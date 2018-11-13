from flask import Flask, render_template
import urllib, json
from util import nasa

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", img = "https://www.dailydot.com/wp-content/uploads/2018/04/ledragondoge-760x400.png")
