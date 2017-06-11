# src/__init__.py
from datetime import date
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import app_config
from src.common.database import Database
from src.domain.reports import createReportsService
from src.domain.users import createUserService
from src.web.auth import auth
from src.web.home import home
from src.web.reports import reports

login_manager = LoginManager()

def start(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Database.initialize(app.config['DATABASE_CONNECTION_URI'])
    services = {
        'userService': createUserService(Database),
        'reportsService': createReportsService(Database)
    }

    @login_manager.user_loader
    def load_user(user_id):
        return services['userService'].getUserByID(user_id)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    Bootstrap(app)

    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(reports)

    return app
