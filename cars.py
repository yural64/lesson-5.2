class Car:
    def __init__(self, make, model):
        self.public_make = make # открытый атрибут Производитель
        self._protected_model = model # защищенный атрибут Модель
        self.__private_year = 2024 # приватный атрибут Год

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_make} {self._protected_model}"

    def _protected_method(self):
        return "Это защищенный метод"

    def __private_method(self):
        return "Это приватный метод"


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_cize = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защищенному атрибутам, но не к приватному
        details = f"{self.public_make} {self._protected_model}, Батарея: {self.battery_cize} kWh."
        # Нельзя напрямую обратиться к __private_method и __private_year
        return details

# Создание экземпляра ElectricCar
tesla = ElectricCar("Tesla", "Model S", 100)

# Доступ к открытому атрибуту и методу:
print(tesla.public_make)
print(tesla.public_method())

# Доступ к защищенному атрибуту (не рекомендуется, но возможно):
print(tesla._protected_model)
print(tesla._protected_method())

# Доступ к приватному атрибуту и методу напрямую невозможет, но можно обойти это ограничение (не рекомендуется):
print(tesla._Car__private_year) # доступ к приватному атрибуту через mandling

