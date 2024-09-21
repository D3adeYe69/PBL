from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pbl21'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended

    db.init_app(app)

    return app
