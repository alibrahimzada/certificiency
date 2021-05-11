from data.models.base_entity import BaseEntity

class Event(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Event, self).__init__()

    def get_all_events(self):
        return self.sql_helper.get_rows('Event')

    def insert_event(self, data):
        query = """INSERT INTO \"Event\"
                   values({}, '{}');""".format(data['event_id'], data['event_name'])

        try:        
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {"status": "success"}
            return {"status": "fail"}
        
        except:
            return {"status": "fail"}

    def delete_event(self, data):
        query = """ 
                DELETE FROM \"Event\"
                WHERE event_id={}""".format(data['event_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}

    def update_event(self, data):
        query = """
            UPDATE \"Event\"
            SET event_name = '{}'
            WHERE event_id={}""".format(data['event_name'], data['event_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}
