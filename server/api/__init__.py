from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

DB_URL = os.environ["DB_URL"]

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'My First API !!'

