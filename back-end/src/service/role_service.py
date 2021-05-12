from service import Service
from data.models.role import Role

class RoleService(Service):

    def __init__(self):
        self.role = Role()

    def get_roles(self):
        return self.role.get_all_roles()

    def insert_role(self, data):
        return self.role.insert_role(data)

    def delete_role(self, data):
        return self.role.delete_role(data)

    def update_role(self, data):
        return self.role.update_role(data)