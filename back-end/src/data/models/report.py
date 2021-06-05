from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Report(BaseEntity):

    def __init__(self):
        super(Report, self).__init__()
  
    def get_event_report(self, event_id):
        data = {}
        data['number_of_applications'] = self.get_num_of_applications_of_event(event_id)
        data['number_of_absents'] = self.get_num_of_absents_of_event(event_id)
        data['numbers_of_attendents'] = self.get_num_of_attendents_of_event(event_id)

        return {'status': 200, 'success': True, 'errors': [], 'data': data}


    def get_event_category_report(self, event_category_id):
        stats = {}
        total_events = self.get_total_events_of_event_cat(event_category_id)
        
        stats['total_events_per_event_cat'] = total_events
        return {'status': 200, 'success': True, 'errors': [], 'data': stats}


    def get_customer_report(self, customer_id):
        stats = {}
        user_stats = self.get_customer_user_stats(customer_id)
        event_stats = self.get_customer_event_stats(customer_id)
        stats['user_count'] = user_stats
        stats['event_count'] = event_stats
        
        return {'status': 200, 'success': True, 'errors': [], 'data': stats}


    def get_user_report(self, user_id):
        data = {}
        data['number_of_applications'] = self.get_num_of_applications_of_user(user_id)
        data['numbers_of_attendents'] = self.get_num_of_attendents_of_user(user_id)

        return {'status': 200, 'success': True, 'errors': [], 'data': data}


    def get_num_of_applications_of_event(self, event_id):
        query =  """ SELECT COUNT(*)
                     FROM applications a
                     WHERE {} = a.event_id   
        """.format(event_id)

        result = self.sql_helper.query_all(query)

        return result[0][0]

    
    def get_num_of_absents_of_event(self, event_id):
        query = """ SELECT COUNT(*)
                    FROM applications a
                    WHERE a.event_id = {} AND a.application_status = 2 
        """.format(event_id)
        
        result = self.sql_helper.query_all(query)

        return result[0][0]
        
    
    def get_num_of_attendents_of_event(self, event_id):
        query = """ SELECT COUNT(*)
                    FROM applications a
                    WHERE a.event_id = {} AND a.application_status = 1
        """.format(event_id)
        
        result = self.sql_helper.query_all(query)
        
        return result[0][0]


    def get_total_events_of_event_cat(self, event_category_id):
        query = """ SELECT COUNT(event_id)
                    FROM events
                    WHERE event_category_id = {}
                """.format(event_category_id)

        result = self.sql_helper.query_all(query)
        return result[0][0]


    def get_customer_user_stats(self, customer_id):
        query = """ SELECT COUNT(user_id)
                    FROM users
                    WHERE customer_id = {}
                """.format(customer_id)

        result = self.sql_helper.query_all(query)

        return result[0][0]
        

    def get_customer_event_stats(self, customer_id):
        query = """ SELECT COUNT(event_id)
                    FROM events
                    WHERE customer_id = {}
                """.format(customer_id)

        result = self.sql_helper.query_all(query)

        return result[0][0]


    def get_num_of_applications_of_user(self, user_id):
        query = """ SELECT COUNT(*)
                    FROM applications
                    WHERE user_id = {}  
        """.format(user_id)

        result = self.sql_helper.query_all(query)

        return result[0][0]


    def get_num_of_attendents_of_user(self, user_id):
        query = """ SELECT COUNT(*)
                    FROM applications
                    WHERE user_id = {} AND application_status = 1
        """.format(user_id)

        result = self.sql_helper.query_all(query)

        return result[0][0]


    def get_customer_stats(self, core_app_context):
        stats = {}
        stats['user_count'] = self.get_num_of_users_of_customer(core_app_context)
        stats['event_count'] = self.get_num_of_events_of_customer(core_app_context)
        stats['application_count'] = self.get_num_of_applications_of_customer(core_app_context)
        stats['certificate_count'] = self.get_num_of_certificates_of_customer(core_app_context)

        return {'status': 200, 'success': True, 'errors': [], 'data': stats}        

    def get_num_of_users_of_customer(self, core_app_context):
        query = """ SELECT COUNT(user_id)
                    FROM users
                    WHERE customer_id = {}
                """.format(core_app_context.customer_id)

        result = self.sql_helper.query_all(query)
        return result[0][0]


    def get_num_of_events_of_customer(self, core_app_context):
        query = """ SELECT COUNT(event_id)
                    FROM events
                    WHERE customer_id = {}
                """.format(core_app_context.customer_id)

        result = self.sql_helper.query_all(query)
        return result[0][0]


    def get_num_of_applications_of_customer(self, core_app_context):
        query = """ SELECT COUNT(*)
                    FROM events e, applications a
                    WHERE e.customer_id = {} AND
                    e.event_id = a.event_id
                """.format(core_app_context.customer_id)

        result = self.sql_helper.query_all(query)
        return result[0][0]


    def get_num_of_certificates_of_customer(self, core_app_context):
        query = """ SELECT COUNT(certificate_id)
                    FROM certificates
                    WHERE application_id IN (
                        SELECT a.application_id
                        FROM events e, applications a
                        WHERE e.customer_id = {} AND
                        e.event_id = a.event_id
                    )
                """.format(core_app_context.customer_id)
        
        result = self.sql_helper.query_all(query)
        return result[0][0]
