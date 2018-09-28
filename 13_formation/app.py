from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def test():
	return render_template("test.html")

@app.route("/auth", methods=['GET', 'POST'])
def authorize():
	print(app)
	print(request)
	print(request.args)
	print(request.headerst)
	return render_template("form.html", firstname=request.args['firstname'], lastname=request.args['lastname'], request_type=request.method)

app.debug = True
if __name__ == "__main__":
	app.run()
