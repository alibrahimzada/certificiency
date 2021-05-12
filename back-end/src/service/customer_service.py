from service import Service
from data.models.customer import Customer

class CustomerService(Service):

    def __init__(self):
        self.customer = Customer()

    def get_customers(self):
        return self.customer.get_all_customers()

    def insert_customer(self, data):
        return self.customer.insert_customer(data)

    def delete_customer(self, data):
        return self.customer.delete_customer(data)

    def update_customer(self, data):
        return self.customer.update_customer(data)
