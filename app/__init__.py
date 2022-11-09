from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Tells python that this is a Flask app. __name__ is a predefined python variable that will change according to the name of the module.
app = Flask(__name__)

# Tells Flask to read and apply the config file.
app.config.from_object(Config)

# A db object representing the database.
db = SQLAlchemy(app)

# An object representing the migration engine. Allows changes to be made to a database.
migrate = Migrate(app, db)

# This will contain the different view functions (routes) used by the app.
from app import routes, models