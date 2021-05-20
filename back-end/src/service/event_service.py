from src.service import Service
from src.data.models.event import Event

class EventService(Service):

    def __init__(self):
        self.event = Event()

    def get_events(self):
        return self.event.get_all_events()

    def get_event(self, event_id):
        return self.event.get_event(event_id)

    def insert_event(self, data):
        return self.event.insert_event(data)

    def delete_event(self, data):
        return self.event.delete_event(data)

    def update_event(self, data):
        return self.event.update_event(data)
