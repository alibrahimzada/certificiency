from service import Service
from data.models.user import User

class UserService(Service):

    def __init__(self):
        self.user = User()

    def get_users(self):
        return self.user.get_all_users()

    def get_user(self, user_id):
        return self.user.get_user(user_id)

    def insert_user(self, data):
        return self.user.insert_user(data)

    def delete_user(self, data):
        return self.user.delete_user(data)

    def update_user(self, data):
        return self.user.update_user(data)
