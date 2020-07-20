from flask import Flask
from flask_restful import Api
from resources.event import EventListResource, EventResource, EventPublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(EventListResource, "/events")
api.add_resource(EventResource, "/events/<int:event_id>")
api.add_resource(EventPublishResource, "/events/<int:event_id>/publish")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
