from . import db
from flask_login import UserMixin
class users (UserMixin, db.Model):
    user_id = db.Column(db.Integer , primary_key=True)
    username= db.Column(db.String(100),unique=True, nullable=False)
    password= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    def __repr__(self):
        return '<User %r>' % self.username