class Vector:

    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        if self.values:
            return f"Вектор({', '.join(map(str,self.values))})"
        return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda v: v+other, self.values)))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*list(map(lambda elem: elem[0]+elem[1], zip(self.values, other.values))))
            else:
                 print("Сложение векторов разной длины недопустимо")
                 return False
        print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda v: v*other, self.values)))
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*list(map(lambda elem: elem[0]*elem[1], zip(self.values, other.values))))
            else:
                 print( "Умножение векторов разной длины недопустимо")
                 return False
        print(f"Вектор нельзя умножать с {other}")



v1 = Vector(1,2,3)
print("Вектор(1, 2, 3)", v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print("Вектор(3, 4, 5)", v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print("Вектор(4, 6, 8)", v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print("Вектор(9, 11, 13)", v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print("Вектор(2, 4, 6)", v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
