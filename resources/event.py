from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.event import Event, event_list


class EventListResource(Resource):
    def get(self):
        data = []
        for event in event_list:
            if event.is_publish is True:
                data.append(event.data)
        return {"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        event = Event(
            name=data["name"],
            description=data["description"],
            date_added=data["date_added"],
            date_event=data["date_event"],
        )
        event_list.append(event)
        return event.data, HTTPStatus.CREATED


class EventResource(Resource):
    def get(self, event_id):
        event = next(
            (
                event
                for event in event_list
                if event.id == event_id and event.is_publish == True
            ),
            None,
        )
        if event is None:
            return {"message": "Event not found"}, HTTPStatus.NOT_FOUND
        return event.data, HTTPStatus.OK

    def put(self, event_id):
        data = request.get_json()
        event = next(
            (
                event
                for event in event_list
                if event.id == event_id and event.is_publish == True
            ),
            None,
        )
        if event is None:
            return {"message": "Event not found"}, HTTPStatus.NOT_FOUND

        event.name = data["name"]
        event.description = data["description"]
        event.date_added = data["date_added"]
        event.date_event = data["date_event"]
        return event.data, HTTPStatus.OK


class EventPublishResource(Resource):
    def put(self, event_id):
        event = next((event for event in event_list if event.id == event_id), None,)
        if event is None:
            return {"message": "Event not found"}, HTTPStatus.NOT_FOUND
        event.is_publish = True
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, event_id):
        event = next((event for event in event_list if event.id == event_id), None,)
        if event is None:
            return {"message": "Event not found"}, HTTPStatus.NOT_FOUND
        event.is_publish = False
        return {}, HTTPStatus.NO_CONTENT
