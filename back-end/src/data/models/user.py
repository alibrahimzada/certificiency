from data.models.base_entity import BaseEntity

class User(BaseEntity):

    # put variables to init
    def __init__(self):
        super(User, self).__init__()
    
    def createUser(self):
        pass
    
    def getAllUsers(self):
        sql = """SELECT display_name AS DisplayName
                 FROM \"Users\""""

        users = self.sql_helper.query_all(sql)

        return users