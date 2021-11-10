class Person:
    def __init__(self,name,surname,gender='male'):
        self.name = name
        self.surname = surname
        if gender not in ['male','female']:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'
        else:
            self.gender = gender
    def __str__(self) -> str:
        return f"Гражданин {self.surname} {self.name}" if self.gender == 'male' else f"Гражданка {self.surname} {self.name}"


p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"
