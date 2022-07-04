from flask import Flask
from flask_mongoengine import MongoEngine
import certifi
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__)
CORS(app)

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.develmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'KFRMCDYLD6VPH3WDOAAEWAK6JU'
app.config['MAIL_PASSWORD'] = 'BNR4QS5MALMJLFI37PHN2F5KWI'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_curd',
    'host': 'mongodb+srv://tikasah84:flask@cluster0.prgdeyb.mongodb.net/?retryWrites=true&w=majority',
    'port': 27017,
    'tlsCAFile': certifi.where()
}

db = MongoEngine()
db.init_app(app)

from crud import routes

