from flask import Flask
from app.extensions import db, migrate
from app.config import Config
from app.routes import api_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
