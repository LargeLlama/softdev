from flask import Flask, render_template, session, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

login_info = { 'rubinpeci' : 'albania123'}

@app.route("/")
def homepage():
	if 'rubinpeci' in session:
		return render_template('welcome.html', username='rubinpeci')
	else:
		return render_template('login.html')

@app.route("/auth", methods=['POST'])
def logged_in():
	if request.form['username'] not in login_info.keys():
		return render_template('login.html', error = "USERNAME INVALID")
	elif login_info[request.form['username']] != request.form['password']:
		return render_template('login.html', error = "PASSWORD INVALID")
	else:
		session[request.form['username']] = request.form['password']
		return redirect(url_for('homepage'))
 
@app.route("/logout", methods=['POST'])
def logout():
	session.pop('rubinpeci')
	return redirect(url_for('homepage'))

if __name__ == '__main__':
	app.debug = True
	app.run()
