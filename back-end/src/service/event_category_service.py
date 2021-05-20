from src.service import Service
from src.data.models.event_category import EventCategory

class EventCategoryService(Service):

    def __init__(self):
        self.event_category = EventCategory()

    def get_event_categories(self):
        return self.event_category.get_all_event_categories()

    def get_event_category(self, event_category_id):
        return self.event_category.get_event_category(event_category_id)

    def insert_event_category(self, data):
        return self.event_category.insert_event_category(data)

    def delete_event_category(self, data):
        return self.event_category.delete_event_category(data)

    def update_event_category(self, data):
        return self.event_category.update_event_category(data)
