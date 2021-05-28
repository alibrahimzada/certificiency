from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Customer(BaseEntity):
    def __init__(self):
        super(Customer, self).__init__()
  
    def get_all_customers(self):
        query = """ SELECT *
                    FROM customers
                    WHERE is_deleted=false
                """
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows(query, 'customers')
        api_response['data'] = rows
        return api_response

    def get_customer(self, customer_id):
        api_response = {'status': 200, 'success': True, 'errors': []}
        customer_data = self.sql_helper.get_single_instance('customers', 'customer_id', customer_id)
        api_response['data'] = customer_data
        return api_response
        
    def insert_customer(self, data):
        query = """INSERT INTO \"customers\" (customer_id, customer_name, is_active, created_on, company_permissions, is_deleted, domain_name)
                   values(DEFAULT, '{}', '{}', '{}', '{}', '{}', '{}')
                """.format(data['customer_name'], True, data['created_on'],
                           data['company_permissions'], False, data['domain_name'])

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion into CUSTOMERS table unsuccessful']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Customer with id = {} already exists'.format(data['customer_id'])]}

    def delete_customer(self, customer_id):
        query = """UPDATE \"customers\"
                   SET is_deleted = 'true' 
                   WHERE customer_id={}
                """.format(customer_id)

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of customer with id = {} from CUSTOMERS table unsuccessful'.format(data['customer_id'])]}

    def update_customer(self, data):
        query = """UPDATE \"customers\"
                   SET customer_name='{}', company_permissions='{}', domain_name='{}'
                   WHERE customer_id={}
                """.format(data['customer_name'], data['company_permissions'], data['domain_name'],
                           data['customer_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error! Updating of customer with id = {} from CUSTOMERS table unsuccessful'.format(data['customer_id'])]}


    def make_active(self, customer_id):
        query = """UPDATE \"customers\"
                   SET is_active = 'true'
                   WHERE customer_id={}
                """.format(customer_id)
                
        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error while updating']}


    def make_passive(self, customer_id):
        query = """ UPDATE \"customers\"
                    SET is_active = 'false'
                    WHERE customer_id={}
                """.format(customer_id)

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error while updating'.format(customer_id)]}
