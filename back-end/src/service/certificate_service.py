from service import Service
from data.models.certificate import Certificate

class CertificateService(Service):

    def __init__(self):
        self.certificate = Certificate()

    def get_certificates(self):
        return self.certificate.get_all_certificates()

    def create_certificate(self, data):
        return self.certificate.insert_certificate(data)

    def delete_certificate(self, data):
        return self.certificate.delete_certificate(data)

    def update_certificate(self, data):
        return self.certificate.update_certificate(data)
