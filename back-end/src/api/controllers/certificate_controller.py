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

@bp.route('/insert-certificate', methods=['POST'])
def insert_certificate():
    """
        This is the endpoint for creating a new certificate
    """

    data = request.get_json()
    status = certificate_service.create_certificate(data)
    return status

@bp.route('/delete-certificate', methods=['DELETE'])
def delete_certificate():
    """
        This is endpoint for deleting a certificate 
    """
    data = request.get_json()
    status = certificate_service.delete_certificate(data)
    return status

@bp.route('/update-certificate', methods=['PUT'])
def update_certificate():
    """
        This is endpoint for updating a certificate 
    """
    data = request.get_json()
    status = certificate_service.update_certificate(data)
    return status
