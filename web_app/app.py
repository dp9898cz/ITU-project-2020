from flask import Flask

from web_app.extensions import db
from web_app.commands import register_commands
from web_app.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    app.register_blueprint(routes)
    db.init_app(app)
    register_commands(app)
    return app

