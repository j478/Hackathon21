from flask import Flask, render_template, request, jsonify, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sqlite3
import os

app = Flask(__name__,
			template_folder='templates',
			static_folder='static',
			static_url_path='/static')

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # prevents the browser from caching files
app.config['SECRET_KEY'] = "MySecretKey"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class providers(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	username = db.Column(db.String(100))
	password = db.Column(db.String(100))
	compName = db.Column(db.String(100))
	salesRep = db.Column(db.String(100))
	isAdmin = db.Column(db.Boolean(False))


	def __init__(self, username, password, compName, salesRep, isAdmin):
		self.username = username
		self.password = password
		self.compName = compName
		self.salesRep = salesRep
		self.isAdmin = isAdmin

def connect():
    return sqlite3.connect("data.db")

class drugsInStock(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	stock = db.Column(db.Integer)
	
	def __init__(self, name, stock):
		self.name = name
		self.stock = stock

class drugsPerscribed(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	numGiven = db.Column(db.Integer)
	
	def __init__(self, name, numGiven):
		self.name = name
		self.numGiven = numGiven
		

#loginForm
class loginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')

@app.route('/dashboard')
def dashboard():

	return render_template('dashboard.html')

@app.route('/inventory')
def inventory():

	return render_template('inventory.html')

@app.route('/medications')
def medications():

	return render_template('medications.html')

@app.route('/contact')
def contact():

	return render_template('contact.html')
	
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
		name = request.form['username'];
		passw = request.form['password'];
		potential_user = providers.query.filter_by(username=name).first()
		if potential_user:
			if potential_user.password == passw:
				return redirect('/dashboard')
			else:
				return redirect('/')
		else:
			return redirect('/')

@app.route("/contact_form_submitted", methods=('POST'))
def contact_form_submitted():
	
	return render_template('contactFormSuccess.html')

			
@app.route("/graph_info", methods=['GET'])
def graph_info():
	drugNames = len(drugsPerscribed.query.all())
	namesList = []
	for i in range(1,drugNames):
		namesList.append(drugsPerscribed.query.get(i).name)
	drugLen = len(drugsPerscribed.query.all())
	perscList = []
	for i in range(1,drugLen):
		perscList.append(drugsPerscribed.query.get(i).numGiven)
	stockList = []
	for i in range(1,drugLen):
		stockList.append(drugsInStock.query.get(i).stock)
		myList = [namesList,perscList,stockList]
	return jsonify({ 'obj':myList })


if __name__ == '__main__':
	app.run()