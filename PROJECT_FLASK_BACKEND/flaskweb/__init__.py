from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import sqlite3
from flask_bcrypt import Bcrypt 


app = Flask(__name__)
app.config['SECRET_KEY']='a4e1dc26b9a8a8c4cf6996342eb212f0'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
from flaskweb import routes
