from service import Service
from data.models.application import Application

class ApplicationService(Service):

    def __init__(self):
        self.application = Application()

    def get_applications(self):
        return self.application.get_all_applications()

    def create_application(self, data):
        return self.application.insert_application(data)

    def delete_application(self, data):
        return self.application.delete_application(data)

    def update_application(self, data):
        return self.application.update_application(data)
