from flask import Flask

from .commands import create_tables
from .extensions import db, login_manager
from .models import User
from .routes.main import main
from .routes.auth import auth


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config['SECRET KEY'] = 'shsshsjfhf38384844dff8f8fd8dv8vf888f8f8ff8'

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app
