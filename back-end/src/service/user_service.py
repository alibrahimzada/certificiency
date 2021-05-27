from src.service import Service
from src.data.models.user import User
from src.service.helpers.crypto_helper import CryptoHelper
import datetime

class UserService(Service):

    def __init__(self):
        self.user = User()
        self.crypto_helper = CryptoHelper()

    def get_users(self):
        return self.user.get_all_users()

    def get_user(self, user_id):
        return self.user.get_user(user_id)

    def insert_user(self, data, core_app_context):
        encrypted_password = self.encrypt_password(data)
        data['password'] = encrypted_password
        data['created_on'] = datetime.datetime.now()
        return self.user.insert_user(data, core_app_context)

    def delete_user(self, user_id):
        return self.user.delete_user(user_id)

    # TODO: perform password encryption here as well
    def update_user(self, data):
        return self.user.update_user(data)

    def encrypt_password(self, data):
        encrypted_password = self.crypto_helper.sha256_encrypt(data['username'], data['password'])
        return encrypted_password
