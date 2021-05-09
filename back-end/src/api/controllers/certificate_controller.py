# from api import app
from service.certificate_service import CertificateService
# from service.user import UserService
# put __init__.py files in each directory
from flask import jsonify, Blueprint, request

certificate_service = CertificateService()

bp = Blueprint('certificate', __name__)
@bp.route('/get-certificates', methods=['GET'])
def get_certificates():
    """
        This is the endpoint returning certificate list
    """
    certificates = certificate_service.get_certificates()

    return jsonify(certificates)

@bp.route('/create-certificate', methods=['POST'])
def create_certificate():
    """
        This is the endpoint for creating a new certificate
    """

    data = request.get_json()
    certificate_service.create_certificate(data)

    return 'worked'


@bp.route('/delete-certificate', methods=['DELETE'])
def delete_certificate():
    """
        This is endpoint for deleting a certificate 
    """
    data = request.get_json()
    certificate_service.certificate_event(data)
    print(data)
    return "deleted"


@bp.route('/update-certificate', methods=['PUT'])
def update_certificate():
    """
        This is endpoint for updating a certificate 
    """
    data = request.get_json()
    certificate_service.update_certificate(data)
    return "updated"
