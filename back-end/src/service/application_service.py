from src.service import Service
from src.data.models.application import Application

class ApplicationService(Service):

    def __init__(self):
        self.application = Application()

    def get_applications(self):
        return self.application.get_all_applications()

    def get_application(self, application_id):
        return self.application.get_application(application_id)

    def create_application(self, data):
        return self.application.insert_application(data)

    def delete_application(self, data):
        return self.application.delete_application(data)

    def update_application(self, data):
        return self.application.update_application(data)

    def update_application_status(self, data):
        return self.application.update_application_status(data)