from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from app.routes import *
import jwt



from connection import create_tables


app = Flask(__name__)
CORS(app)

Compress(app)
create_tables()