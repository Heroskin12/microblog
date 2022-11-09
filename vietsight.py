from app import app, db
from app.models import User, Post

# Allows running of the Python command terminal without having to constantly import the app or db.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}