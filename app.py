from flask import Flask
from models import db   # import the db object, not everything with *

app = None

def setup_app():
    global app
    app = Flask(__name__)

    # Correct config key
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hms.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # optional, avoids warnings

    db.init_app(app)  # link db with app
    print("HMS app setup done....")

    app.app_context().push()  # push context so models can use it

    print("HMS app setup done....")

setup_app()

from controller import *

if __name__ == "__main__":
    app.run(debug=True)
