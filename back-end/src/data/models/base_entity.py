from src.data.helpers.sql_helper import SqlHelper

class BaseEntity:

    def __init__(self):
        self.sql_helper = SqlHelper()