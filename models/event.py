event_list = []


def get_last_id():
    if event_list:
        last_event = event_list[-1]
    else:
        return 1
    return last_event.id + 1


class Event:
    def __init__(self, name, description, date_added, date_event):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.date_added = date_added
        self.date_event = date_event
        self.is_publish = False

    @property
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_added": self.date_added,
            "date_event": self.date_event,
        }
