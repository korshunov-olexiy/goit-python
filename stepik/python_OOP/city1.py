class City:
    
    def __init__(self, name):
        self.name = ' '.join([n.capitalize() for n in name.split()])

    def __str__(self):
        return self.name
    
    def __bool__(self):
        return False if self.name[-1] in 'aeiou' else True


p1 = City('new york')
print("New York", p1)  # печатает "New York"
print(True, bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print("San Francisco", p2)  # печатает "San Francisco"
print(False, p2 == True)  # печатает "False"
