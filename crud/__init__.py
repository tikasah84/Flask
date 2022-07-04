from flask import Flask
from flask_mongoengine import MongoEngine
import certifi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_curd',
    'host': 'mongodb+srv://tikasah84:flask@cluster0.prgdeyb.mongodb.net/?retryWrites=true&w=majority',
    'port': 27017,
    'tlsCAFile': certifi.where()
}

db = MongoEngine()
db.init_app(app)

from crud import routes

