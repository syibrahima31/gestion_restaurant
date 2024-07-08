from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    from .views import menu_views, auth_views, admin_views
    app.register_blueprint(menu_views.menu_bp)
    app.register_blueprint(auth_views.auth_bp)
    app.register_blueprint(admin_views.admin_bp)
    return app 