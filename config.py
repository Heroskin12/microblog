import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Alchemy takes location of database from the URI variable below.
    # If Alchemy finds no database in DATABASE_URL, it creates one called app.db in the basedir variable set above.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Set below to False to stop sending a signal to the app each time a DB change is about to be made.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

