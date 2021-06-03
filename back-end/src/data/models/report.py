# TODO Numbers of Applications for specific event, with absent and attended details. (Beyza)
# TODO Rate of attendance per user (Beyza)
from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Report(BaseEntity):

    def __init__(self):
        super(Report, self).__init__()
  

    def get_num_of_applications(self, event_id):
        query =  """ SELECT COUNT(*)
                     FROM applications a
                     WHERE {} = a.event_id   
        """.format(event_id)

        result = self.sql_helper.query_all(query)

        return result

    
    def get_num_of_absents(self, event_id):
        query = """ SELECT COUNT(*)
                    FROM applications a
                    WHERE a.event_id = {} AND a.application_status = 2 
        """.format(event_id)
        
        result = self.sql_helper.query_all(query)

        return result
        
    
    def get_num_of_attendents(self, event_id):
        query = """ SELECT COUNT(*)
                    FROM applications a
                    WHERE a.event_id = {} AND a.application_status = 1
        """.format(event_id)
        
        result = self.sql_helper.query_all(query)
        
        return result


    def get_event_applications_details(self, event_id):
        data = {}
        data['number_of_applications'] = self.get_num_of_applications(event_id)[0][0]
        data['number_of_absents'] = self.get_num_of_absents(event_id)[0][0]
        data['numbers_of_attendents'] = self.get_num_of_attendents(event_id)[0][0]
        return data


    def get_total_events_per_event_cat(self):
        query = """ SELECT COUNT(event_id), event_category_id
                    FROM events
                    GROUP BY event_category_id
                """

        result = self.sql_helper.query_all(query)
        data = self.jsonify_result(result)

        return {'status': 200, 'success': True, 'errors': [], 'data': data}

    def get_customer_stats(self):
        stats = {}
        user_stats = self.get_customer_user_stats()
        event_stats = self.get_customer_event_stats()
        stats['user_stats'] = user_stats
        stats['event_stats'] = event_stats
        
        return {'status': 200, 'success': True, 'errors': [], 'data': stats}

    def get_customer_user_stats(self):
        query = """ SELECT COUNT(user_id), customer_id
                    FROM users
                    GROUP BY customer_id
                """

        result = self.sql_helper.query_all(query)
        data = self.jsonify_result(result)
        return data
        
    def get_customer_event_stats(self):
        query = """ SELECT COUNT(event_id), customer_id
                    FROM events
                    GROUP BY customer_id
                """

        result = self.sql_helper.query_all(query)
        data = self.jsonify_result(result)
        return data

    def jsonify_result(self, result):
        data = {}
        for i in range(len(result)):
            count = result[i][0]
            key = result[i][1]
            data[str(key)] = count

        return data
