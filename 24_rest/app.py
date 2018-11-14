from flask import Flask, render_template
import urllib, json
from util import nasa

app = Flask(__name__)

@app.route("/")
def home():
    dict = nasa.get_dict()
    if dict["media_type"] == "video":
        return render_template("video.html", url = dict['url'], desc = dict['explanation'])
    else:
        return render_template("image.html", img = dict['url'], desc = dict['explanation'])
