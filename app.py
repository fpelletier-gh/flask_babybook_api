from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import Config
from extensions import db
from models.user import User
from resources.event import EventListResource, EventResource, EventPublishResource
from resources.user import UserListResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, "/users")
    api.add_resource(EventListResource, "/events")
    api.add_resource(EventResource, "/events/<int:event_id>")
    api.add_resource(EventPublishResource, "/events/<int:event_id>/publish")


if __name__ == "__main__":
    app = create_app()
    app.run()
