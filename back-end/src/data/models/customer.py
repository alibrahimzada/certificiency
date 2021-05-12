from data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Customer(BaseEntity):
    def __init__(self):
        super(Customer, self).__init__()
  
    def get_all_customers(self):
        api_response = {'status': 200, 'success': True, 'errors': []}
        rows = self.sql_helper.get_rows('customers')
        api_response['data'] = rows
        return api_response

    def insert_customer(self, data):
        query = """INSERT INTO \"customers\"
                   values({}, '{}', '{}', '{}', '{}', '{}')
                """.format(data['customer_id'], data['customer_name'],
                           data['is_active'], data['created_on'],
                           data['company_permissions'], data['is_deleted'])

        try:
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {'status': 200, 'success': True, 'errors': []}

            return {'status': 500, 'success': False, 'errors': ['Error! Insertion into CUSTOMERS table unsuccessful']}
        
        except UniqueViolation:
            return {'status': 400, 'success': False, 'errors': ['Error! Customer with id = {} already exists'.format(data['customer_id'])]}

    def delete_customer(self, data):
        query = """DELETE FROM \"customers\"
                   WHERE customer_id={}
                """.format(data['customer_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}
        
        return {'status': 500, 'success': False, 'errors': ['Error! Deletion of customer with id = {} from CUSTOMERS table unsuccessful'.format(data['customer_id'])]}

    def update_customer(self, data):
        query = """UPDATE \"customers\"
                   SET customer_name='{}', is_active='{}', created_on='{}', company_permissions='{}', is_deleted='{}'
                   WHERE customer_id={}
                """.format(data['customer_name'], data['is_active'], data['created_on'],
                           data['company_permissions'], data['is_deleted'], data['customer_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 200, 'success': True, 'errors': []}

        return {'status': 500, 'success': False, 'errors': ['Error! Updating of customer with id = {} from CUSTOMERS table unsuccessful'.format(data['customer_id'])]}
