from util import words, forecast, chuck

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    tmp_word = request.args.get('search', 'lacrosse') 
    tmp = words.get_definition(tmp_word)

    weather_temp = forecast.get_temp(40.718, -74.014)
    weather_summary = forecast.get_summary(40.718, -74.014)

    chuck_joke = chuck.get_joke()

    return render_template("home.html", word = tmp_word, definition = tmp, temp = str(weather_temp) + " Degrees Farenheit" , summary = weather_summary, joke = chuck_joke)
