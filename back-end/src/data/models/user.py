from data.models.base_entity import BaseEntity

class User(BaseEntity):

    # put variables to init
    def __init__(self):
        super(User, self).__init__()
  
    def get_all_users(self):
        return self.sql_helper.get_rows('User')

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
