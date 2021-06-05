from src.service import Service
from src.data.models.application import Application
import datetime

class ApplicationService(Service):

    def __init__(self):
        self.application = Application()

    def get_applications(self, core_app_context):
        return self.application.get_all_applications(core_app_context)

    def get_application(self, application_id):
        return self.application.get_application(application_id)

    def insert_application(self, data, core_app_context):
        # checking if a user already applied to this event
        if self.application.is_application_available(data, core_app_context):
            return {'status': 500, 'success': False, 'errors': ['You have already applied to this event']}

        # checking if there is any quota available for this event
        if not self.application.is_quota_available(data):
            return {'status': 500, 'success': False, 'errors': ['There is no quota available for this event']}

        data['applied_on'] = datetime.datetime.now()
        return self.application.insert_application(data, core_app_context)

    def delete_application(self, application_id):
        return self.application.delete_application(application_id)

    def update_application(self, data):
        return self.application.update_application(data)

    def update_application_status(self, data):
        return self.application.update_application_status(data)
    
    def get_event_applications(self, event_id, core_app_context):
        return self.application.get_event_applications(event_id, core_app_context)
