from src.service import Service
from src.data.models.role import Role

class RoleService(Service):

    def __init__(self):
        self.role = Role()

    def get_roles(self):
        return self.role.get_all_roles()

    def get_role(self, role_id):
        return self.role.get_role(role_id)

    def insert_role(self, data, core_app_context):
        return self.role.insert_role(data, core_app_context)

    def delete_role(self, role_id):
        return self.role.delete_role(role_id)

    def update_role(self, data, core_app_context):
        return self.role.update_role(data, core_app_context)