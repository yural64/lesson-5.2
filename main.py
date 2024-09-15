class Bird(): # Родительский класс
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет - {self.voice}")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас")

class Pigeon(Bird): # Дочерний класс от Bird
    def __init__(self, name, voice, color, favorid_food):
        super().__init__(name, voice, color)
        self.favorid_food = favorid_food # добавили аргумент для класса

    def walk(self): # добавили метод для класса
        print(f"{self.name} гуляет")

#Создаем объект класса Pigeon
bird1 = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")

bird1.sing()
bird1.info()
bird1.walk()