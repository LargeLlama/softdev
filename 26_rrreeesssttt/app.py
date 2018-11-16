from flask import Flask, render_template, session, request
import urllib, json
from util import words

app = Flask(__name__)

@app.route("/")
def home():
    temp_word = request.args.get('search', 'lacrosse') 
    temp = words.get_definition(temp_word)
    return render_template("home.html", word = temp_word, definition = temp)
