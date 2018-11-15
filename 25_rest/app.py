from flask import Flask, render_template
import urllib, json
from util import news

app = Flask(__name__)

@app.route("/")
def home():
    dictionary = news.top_headlines('bbc-news')
    article  = dictionary['articles'][0]['content']
    return render_template('home.html', content = article)
