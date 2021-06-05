from src.service import Service
from src.data.models.report import Report

class ReportService(Service):

    def __init__(self):
        self.report = Report()

    def get_event_report(self, event_id):
        return self.report.get_event_report(event_id)

    def get_customer_report(self, customer_id):
        return self.report.get_customer_report(customer_id)

    def get_event_category_report(self, event_category_id):
        return self.report.get_event_category_report(event_category_id)

    def get_user_report(self, user_id):
        return self.report.get_user_report(user_id)

    def get_customer_stats(self, core_app_context):
        return self.report.get_customer_stats(core_app_context)
