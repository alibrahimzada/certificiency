from src.service import Service
from src.data.models.customer import Customer
import datetime

class CustomerService(Service):

    def __init__(self):
        self.customer = Customer()

    def get_customers(self):
        return self.customer.get_all_customers()

    def get_customer(self, customer_id):
        return self.customer.get_customer(customer_id)

    def insert_customer(self, data):
        data['created_on'] = datetime.datetime.now()
        return self.customer.insert_customer(data)

    def delete_customer(self, customer_id):
        return self.customer.delete_customer(customer_id)

    def update_customer(self, data):
        return self.customer.update_customer(data)

    def make_active(self, customer_id):
        return self.customer.make_active(customer_id)
    
    def make_passive(self, customer_id):
        return self.customer.make_passive(customer_id)
