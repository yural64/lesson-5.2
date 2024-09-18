class User:
    def __init__(self, user_id, user_name, user_access):
        self.user_id = user_id
        self.user_name = user_name
        self.user_access = user_access


class Admin(User):
    def __init__(self, user_id, user_name, user_access, admin_access):
        super().__init__(user_id, user_name, user_access)
        self.admin_access = admin_access

    def add_user(self):
        pass

    def remove_user(self):
        pass
