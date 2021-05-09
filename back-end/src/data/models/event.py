from data.models.base_entity import BaseEntity

class Event(BaseEntity):

    # put variables to init
    def __init__(self):
        super(Event, self).__init__()
    
    def create_event(self):
        pass
    
    def get_column_names(self):
        sql = """SELECT column_name
                 FROM information_schema.columns
                 WHERE table_name = 'Event';"""
        
        column_names = self.sql_helper.query_all(sql)
        return column_names

    def get_all_events(self):
        column_names = self.get_column_names()

        sql = """SELECT *
                 FROM \"Event\""""

        res = self.sql_helper.query_all(sql)

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

        sql = """INSERT INTO \"Event\"
                 VALUES (4, 'Test Event 4')"""
        # print("""INSERT INTO public.\"Event\" (event_id, event_name)
        #          values({}, '{}');""".format(data['event_id'], data['event_name']))
        status = self.sql_helper.execute(sql)
        print(status)
<<<<<<< HEAD


    def delete_event(self, data):
        sql = """ 
            DELETE FROM \"Event\"
            WHERE event_id={}
        """.format(data['event_id'])
        status = self.sql_helper.execute(sql)
        print(status)


    def update_event(self, data):
        sql = """
            UPDATE \"Event\"
            SET 
            WHERE 
        """

        status = self.sql_helper.execute(sql)
        print(status)
=======
>>>>>>> e24cce0ac6988de8e3742919b62e30b5c70ee96a
