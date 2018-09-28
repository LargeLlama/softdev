from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

@app.route("/")
def test():
	# generates a random number between 1-100 and gives a 50/50 chance between making the type post or get
	option = randint(1, 101)
	if option <= 50:
		return render_template("home.html", choice="POST")
	else:
		method = "GET"
		return render_template("home.html", choice="GET")

@app.route("/auth", methods=['GET', 'POST'])
def authorize():
	''' Diagnostic statements
	print(app)
	print(request)
	print(request.args)
	print(request.headers)	
	'''
	#Will do the proper method type based of whatever requests says it is
	if request.method == "POST":
		return render_template("form.html", firstname=request.form['firstname'], lastname=request.form['lastname'], request_type=request.method)
	else:
		return render_template("form.html", firstname=request.args['firstname'], lastname=request.args['lastname'], request_type=request.method)

app.debug = True
if __name__ == "__main__":
	app.run()
