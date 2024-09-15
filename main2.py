class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищенный атрибут"
        self.__private = "приватный атрибут"

    def get_private(self): # "геттер" - берет значение приватного атрибута
        return self.__private

    def set_private(self, value):  # "сеттер" - устанавливает новое значение приватного атрибута
        self.__private = value # записываем значение приватного атрибута

test = Test()
print(test.public)
print(test._protected)
print(test.get_private())

test.set_private("Получили значение приватного атрибута")
print(test.get_private())
