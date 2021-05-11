from data.models.base_entity import BaseEntity

class Event(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Event, self).__init__()

    def get_column_names(self):
        sql = """SELECT column_name
                 FROM information_schema.columns
                 WHERE table_name = 'Event';"""
        
        column_names = self.sql_helper.query_all(sql)
        return column_names

    def get_all_events(self):
        column_names = self.get_column_names()

        query = """SELECT *
                   FROM \"Event\""""

        res = self.sql_helper.query_all(query)

        events = []
        for i in range(len(res)):
            event_details = {}

            for j in range(len(res[i])):
                table_column = column_names[j][0]
                cell_value = res[i][j]

                event_details[table_column] = cell_value
            
            events.append(event_details)

        return events

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
