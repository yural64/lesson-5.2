# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов. У каждого
# сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы,
# помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут
# добавлять или удалять пользователя из системы.

# Требования:

# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень
# доступа ('user' для обычных сотрудников).

# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут
# уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать
# методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).

# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access = "user"


    def get_user_id(self):
        return self._user_id


    def get_name(self):
        return self._name


    def get_user_access(self):
        return self._access


    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._user_access = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список.")
        print(user_list)

    def remove_user(self,user_list, user):
        user_list.remove(user)
        print(f"Пользователь успешно удален из списка.")
        print(user_list)

users = []
admin = Admin("adm1", "Иван")
user1 = User("user01", "Петр")

print(user1.get_name())
admin.add_user(users, user1)

user2 = User("user02", "Ольга")
admin.add_user(users, user2)

admin.remove_user(users, user1)
