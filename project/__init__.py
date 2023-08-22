from flask import Flask
from .utils import make_celery
from .views import main
from .extensions import db
from .tasks import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SECRET_KEY"] = "Oz8Z7Iu&DwoQK)g%*Wit2YpE#-46vy0n"
    app.config["CELERY_CONFIG"] = {
        "broker_url": "redis://redis", 
        "result_backend": "redis://redis", 
        "redbeat_redis_url": "redis://redis"
    }

    db.init_app(app)

    app.register_blueprint(main)

    celery = make_celery(app)
    celery.set_default()

    return app, celery