class Vector:
    def __init__(self, *kwards) -> None:
        self.values = [k for k in kwards if isinstance(k, int)]
    def __str__(self):
        if self.values:
            return f"Вектор({', '.join(map(str,sorted(self.values)))})"
        return "Пустой вектор"

v = Vector(1,2,3)
print(v)
