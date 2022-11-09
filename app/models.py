from datetime import datetime
from app import db

# The ORM will turn the Class model below into sqlite commands.
# db.Model is a base class for all models in SQLAlchemy.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Max length is in brackets to optimise space.
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #db.relationship is normally defined on the 'one' side of a 'one-to-many' relationship. 
    # If I have a user stored in u, u.posts will run a query that returns all posts written by that user.
    # First argument is Class which refers to the 'many'. Author will point back to User.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Tells Python how to print objects of this class. This is useful for debugging.
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # Useful to retrieve posts in chronological order.
    # SQL will set the value of timestamp to the result of the function datetime.utcnow.
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)