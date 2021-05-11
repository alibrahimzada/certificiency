from data.models.base_entity import BaseEntity

class User(BaseEntity):

    # put variables to init
    def __init__(self):
        super(User, self).__init__()
    
    def get_column_names(self):
        sql = """SELECT column_name
                 FROM information_schema.columns
                 WHERE table_name = 'User';"""
        
        column_names = self.sql_helper.query_all(sql)
        return column_names

    def get_all_users(self):
        column_names = self.get_column_names()

        query = """SELECT *
                   FROM \"User\""""

        res = self.sql_helper.query_all(query)

        users = []
        for i in range(len(res)):
            user_details = {}

            for j in range(len(res[i])):
                table_column = column_names[j][0]
                cell_value = res[i][j]

                user_details[table_column] = cell_value
            
            users.append(user_details)

        return users

    def insert_user(self, data):
        query = """INSERT INTO \"User\"
                   values({}, '{}');""".format(data['user_id'], data['user_email'])

        try:        
            rows_affected = self.sql_helper.execute(query)
            if rows_affected > 0:
                return {"status": "success"}
            return {"status": "fail"}
        
        except:
            return {"status": "fail"}

    def delete_user(self, data):
        query = """ 
                DELETE FROM \"User\"
                WHERE user_id={}""".format(data['user_id'])

        rows_affected = self.sql_helper.execute(query)
        
        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}

    def update_user(self, data):
        query = """
            UPDATE \"User\"
            SET user_email = '{}'
            WHERE user_id={}""".format(data['user_email'], data['user_id'])

        rows_affected = self.sql_helper.execute(query)

        if rows_affected > 0:
            return {'status': 'success'}
        return {'status': 'fail'}
