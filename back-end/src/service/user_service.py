from service import Service
from data.models.user import User

class UserService(Service):

    def __init__(self):
        self.user = User()

    def get_users(self):
        users = self.user.getAllUsers()

        return users