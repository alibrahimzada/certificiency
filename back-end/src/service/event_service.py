from service import Service
from data.models.event import Event

class EventService(Service):

    def __init__(self):
        self.event = Event()

    def get_events(self):
        events = self.event.get_all_events()

        return events

    def create_event(self, data):
        self.event.insert_event(data)
        