from src.service import Service
from src.data.models.certificate import Certificate

class CertificateService(Service):

    def __init__(self):
        self.certificate = Certificate()

    def get_certificates(self):
        return self.certificate.get_all_certificates()

    def get_certificate(self, certificate_id):
        return self.certificate.get_certificate(certificate_id)

    def create_certificate(self, data):
        return self.certificate.insert_certificate(data)

    def delete_certificate(self, data):
        return self.certificate.delete_certificate(data)

    def update_certificate(self, data):
        return self.certificate.update_certificate(data)
