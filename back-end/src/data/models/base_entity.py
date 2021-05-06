from data.helpers.sqlHelper import SqlHelper

class BaseEntity:

    def __init__(self):
        self.sql_helper = SqlHelper()