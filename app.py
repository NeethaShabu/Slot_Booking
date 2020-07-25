from flask import Flask, render_template, redirect, url_for, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("Home.html")
	

"""@app.route('/login',methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = "Invalid username or password . Failed to login...."
		else:
			return redirect(url_for('home'))
	return render_template('login.html',error=error)"""


@app.route('/login',methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			return render_template("welcome.html")
		else:
			return redirect(url_for('home'))
	return render_template('login.html',error=error)



"""@app.route('/register',methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		if request.form['user'] != '' and request.form['mail'] != '' and request.form['pass'] !='':
			return render_template("success.html")
		else:
			return redirect(url_for('home'))
	return render_template('register.html',error=error)"""


@app.route('/register',methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		if request.form['user'] != '' and request.form['mail'] != '' and request.form['pass'] !='':
			username = request.form['user']
			password = request.form['pass']
			email = request.form['mail']
			conn = sqlite3.connect("signin.db")
			c= conn.cursor()
			c.execute("INSERT INTO person3 VALUES('"+username+"', '"+email+"' ,'"+password+"')")
			conn.commit()
			conn.close()
			return render_template("success.html")
		else:
			return redirect(url_for('home'))
	return render_template('register.html',error=error)


if __name__ == '__main__':
	app.run(debug=True)