from flask import Flask

from web_app.extensions import db, login_manager
from web_app.commands import register_commands
from web_app.routes import routes
from web_app.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")

    app.register_blueprint(routes)

    login_manager.init_app(app)

    db.init_app(app)

    register_commands(app)

    login_manager.login_view = 'routes.login'
    @login_manager.user_loader
    def loadUser(userID):
        return User.query.get(userID)

    return app
