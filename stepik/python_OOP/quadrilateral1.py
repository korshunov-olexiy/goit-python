class Quadrilateral:
    
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width
    def __str__(self):
        return f"Куб размером {self.width}х{self.height}" if self.width == self.height else f"Прямоугольник размером {self.width}х{self.height}"


q = Quadrilateral(1,1)
print(q)
