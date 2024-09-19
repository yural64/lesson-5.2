

class User():
    def __init__(self, user_id, user_name):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_access = "user"
        self.users = []


def get_user_id(self):
    return self.__user_id

def get_user_name(self):
    return self.__user_name

def get_user_access(self):
    return self.__user_access

def set_user_name(self, user_name):
    self.__user_name - user_name



class Admin(User):
    def __init__(self, user_id, user_name, admin_access):
        super().__init__(user_id, user_name)
        self.admin_access = admin_access

    def add_user(self):
        pass

    def remove_user(self):
        pass
