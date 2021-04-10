from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__,
			template_folder='templates',
			static_folder='static',
			static_url_path='/static')

#ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'PDF', 'PNG', 'JPG', 'JPEG', 'GIF'}
#UPLOAD_FOLDER = 'static/img/uploaded'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#database
db = SQLAlchemy(app)
	_id = db.Column("id", db.Integer, primary_key=True)
	username = db.Column(db.String(100))
	password = db.Column(db.String(100))

	def __init__(self, username, password):
		self.username = username
		self.password = password


@app.route('/')
def index():
	"""
	Serve our app's homepage.
	:return: Jinja2-rendered HTML file.
	"""
	return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_image():
	"""
	Process a file upload to our server.
	:return: JSON data resulting from our processing.
	"""


if __name__ == '__main__':
	db.create_all()
	app.run()
