#Rubin Peci
#Period 7
#Software Development
#2018-09-19

from flask import Flask

app = Flask(__name__)

@app.route('/')
def first_page():
    return 'Hi this is the very first page of my server!'

@app.route('/ligma')
def second_page():
    return "What's ligma?"

@app.route('/ASTROWORLD')
def third_page():
    return "THIRTEEN HOURS TILL I LAND"

app.run()
