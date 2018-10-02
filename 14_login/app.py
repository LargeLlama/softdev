from flask import Flask, render_template, session, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

#dictionary containing login info
login_info = { 'rubinpeci' : 'albania123'}

#root path
@app.route("/")
def homepage():
	#if we're logged in, then return the welcome page
	if 'rubinpeci' in session:
		return render_template('welcome.html', username='rubinpeci')
	else: #otherwise, display the login page
		return render_template('login.html')

#after the user submits their login info, gotta check whether its valid
@app.route("/auth", methods=['POST'])
def logged_in():
	if request.form['username'] not in login_info.keys():
		return render_template('login.html', error = "USERNAME INVALID")
	elif login_info[request.form['username']] != request.form['password']:
		return render_template('login.html', error = "PASSWORD INVALID")
	else: #if we reached this point, that means the username and password match up
		session[request.form['username']] = request.form['password']
		return redirect(url_for('homepage'))
 
#logging out removes our username from the session
@app.route("/logout", methods=['POST'])
def logout():
	session.pop('rubinpeci')
	return redirect(url_for('homepage'))

if __name__ == '__main__':
	app.debug = True
	app.run()
