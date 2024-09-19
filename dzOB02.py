

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
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.__user_access = "admin"

    def add_user(self, users, user):
        users.append(user)
        print(f"Пользователь {user_name} успешно добавлен в список.")

    def remove_user(self):
        users.remove(user)
        print(f"Пользователь {user_name} успешно удален из списка.")
