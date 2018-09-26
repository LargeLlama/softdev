from flask import Flask, render_template
from util import occupations

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("about to print __name__")
    print(__name__)
    return '<h1> Click <a href=/occupations>here</a> to go to the occupations page! </h1>'

#Get the dictionary, create a variable for it so we don't have to call the function more than once
dict = occupations.parse_data('data/occupations.csv')
job = occupations.pick_job(dict)

@app.route('/occupations')
def occupations():
    return render_template('occupations.html', 
                           random_occupation = job,
                           _dict = dict)
                            

app.debug = True
if __name__ == "__main__":
    app.run()
