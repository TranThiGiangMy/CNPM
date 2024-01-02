from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = '&$#%%^^O)(*&^%(*&^$%^&*&^%$#$%^&*&^%$#$%^&^%$#$%^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/manage_flight?charset=utf8mb4' % quote(
    'Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cloudinary.config(cloud_name='dv2y8ynkx',
                  api_key='238948479572549',
                  api_secret='tGIukDd3WlboSNpb-bTYF_MLqTY')

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return 'vi'
