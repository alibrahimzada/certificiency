from src.service import Service
from src.data.models.customer import Customer
from src.service.user_service import UserService
from src.service.role_service import RoleService
from src.service.helpers.request_handler import CoreAppContext
import datetime

class CustomerService(Service):

    def __init__(self):
        self.customer = Customer()
        self.role_service = RoleService()
        self.user_service = UserService()


    def get_customers(self):
        return self.customer.get_all_customers()

    def get_customer(self, customer_id):
        return self.customer.get_customer(customer_id)

    def insert_customer(self, data):
        data['customer']['created_on'] = datetime.datetime.now()

        api_response_customer = self.customer.insert_customer(data['customer'])
        if not api_response_customer['success']:
            return api_response_customer

        customer_id = api_response_customer['data']['customer_id']
        core_app_context = CoreAppContext(-1, customer_id, -1)
        api_response_role = self.role_service.insert_role(data['role'], core_app_context)
        if not api_response_role['success']:
            api_response_customer['errors'].append('Error! Role insertion failed')
            return api_response_customer

        role_id = api_response_role['data']['role_id']
        data['user']['role_id'] = role_id
        api_response_user = self.user_service.insert_user(data['user'], core_app_context)
        if not api_response_user['success']:
            api_response_customer['errors'].append('Error! User insertion failed')
            return api_response_customer

        return api_response_customer

    def delete_customer(self, customer_id):
        return self.customer.delete_customer(customer_id)

    def update_customer(self, data):
        return self.customer.update_customer(data)

    def make_active(self, customer_id):
        return self.customer.make_active(customer_id)
    
    def make_passive(self, customer_id):
        return self.customer.make_passive(customer_id)
