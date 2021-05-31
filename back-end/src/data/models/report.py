# TODO Numbers of Applications for specific event, with absent and attended details. (Beyza)
# TODO Customer statistics for super users --> users of customers, total number of created events (Ali)
# TODO Providing the total number of created events for each event category (Ali)
# TODO Rate of attendance per user (Beyza)
from src.data.models.base_entity import BaseEntity
from psycopg2.errors import UniqueViolation

class Report(BaseEntity):

    def __init__(self):
        super(Report, self).__init__()
  
