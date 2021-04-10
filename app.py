from flask import Flask, render_template, request, jsonify, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
import data.py

app = Flask(__name__,
			template_folder='templates',
			static_folder='static',
			static_url_path='/static')

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # prevents the browser from caching files
app.config['SECRET_KEY'] = "MySecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#database
db = SQLAlchemy(app)

class providers(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	username = db.Column(db.String(100))
	password = db.Column(db.String(100))

	def __init__(self, username, password, info):
		self.username = username
		self.password = password
		self.info = info 

#loginForm
class loginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	
@app.route('/', methods=['POST','GET'])
def login():
	"""
	Serve our app's login page.
	:return: Jinja2-rendered HTML file.
	"""
	form = loginForm()
	return render_template('login.html', form=form)

# Checks login info with database, redirects back to login if false
# Returns Jinja2-rendered HTML file
@app.route("/verify_login", methods=['POST'])
def verify_login():
	if request.method == 'POST':
		if (request.form['username'] == 'Jake' and request.form['password'] == 'D') or (request.form['username'] == 'Caleb' and request.form['password'] == 'B'):
			return redirect('/home')
		else:
			return redirect('/')
			
@app.route("/home")
def home():
	return render_template('home.html')
"""@app.route('/login', methods=['POST','GET'])
def login():
	form = loginForm()
	if form.validate_on_submit:
		print(form.username.data)
		print(form.password.data)
	return render_template('login.html', form=form)
"""

if __name__ == '__main__':
	db.create_all()
	app.run()