from src.service import Service
from src.data.models.customer import Customer
from src.data.models.user import User
from src.data.models.role import Role
from src.service.helpers.request_handler import CoreAppContext
import datetime

class CustomerService(Service):

    def __init__(self):
        self.customer = Customer()
        self.role = Role()
        self.user = User()


    def get_customers(self):
        return self.customer.get_all_customers()

    def get_customer(self, customer_id):
        return self.customer.get_customer(customer_id)

    def insert_customer(self, data):
        data['created_on'] = datetime.datetime.now()
        
        api_response_customer = self.customer.insert_customer(data['customer'])
        customer_id = api_response_customer['data']['customer_id']
        core_app_context = CoreAppContext(-1, customer_id, -1)

        api_response_role = self.role.insert_role(data['role'], core_app_context)
        role_id = api_response_role['data']['role_id']
        data['user']['role_id'] = role_id

        api_response_user = self.user.insert_user(data['user'], core_app_context)

        return api_response_customer

    def delete_customer(self, customer_id):
        return self.customer.delete_customer(customer_id)

    def update_customer(self, data):
        return self.customer.update_customer(data)

    def make_active(self, customer_id):
        return self.customer.make_active(customer_id)
    
    def make_passive(self, customer_id):
        return self.customer.make_passive(customer_id)
