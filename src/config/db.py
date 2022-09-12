from app import app
from flask_sqlalchemy import SQLAlchemy
import os

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db. Column(db.String(100), nullable = False)
    pet_type = db.Column(db.String(100), nullable = False)
    pet_age = db.Column(db.Integer(), nullable = False)
    pet_description = db.Column(db.String(100), nullable = False)


    def __repr__(self):
        return "<Pet %r>" % self.pet_name

db.create_all()
# db.session.commit()