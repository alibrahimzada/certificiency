from src.service import Service
from src.data.models.report import Report

class ReportService(Service):

    def __init__(self):
        self.report = Report()

    def get_event_report(self):
        pass

    def get_customer_report(self):
        pass

    def get_user_report(self):
        pass
