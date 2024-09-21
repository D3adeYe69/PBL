from flask import Flask, request, jsonify, redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
import logging
import os
from dotenv import load_dotenv
db=SQLAlchemy()
login_manager=LoginManager()
def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

    # Check for missing variables and raise an error if any is missing
    for key in ['MYSQL_HOST', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DB']:
        if not app.config[key]:
            raise ValueError(f"Environment variable {key} is not set")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mysql+pymysql://' + app.config['MYSQL_USER'] + ':' + 
        app.config['MYSQL_PASSWORD'] + '@' + app.config['MYSQL_HOST'] + 
        '/' + app.config['MYSQL_DB']
    )
    db.init_app(app)
    
    return app


   

   
    
    