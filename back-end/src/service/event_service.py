from src.service import Service
from src.data.models.event import Event

class EventService(Service):

    def __init__(self):
        self.event = Event()

    def get_events(self):
        return self.event.get_all_events()

    def get_event(self, event_id):
        return self.event.get_event(event_id)

    def insert_event(self, data, core_app_context):
        return self.event.insert_event(data, core_app_context)

    def delete_event(self, event_id):
        return self.event.delete_event(event_id)

    def update_event(self, data):
        return self.event.update_event(data)

    def get_my_events(self, core_app_context):
        return self.event.get_my_events(core_app_context)
