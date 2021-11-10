class ChessPlayer:
    
    def __init__(self,name, surname, rating):
        self.name = name
        self.surname=surname
        self.rating = rating
    
    def __eq__(self, other):
        if isinstance(other, int):
            return True if self.rating == other else False
        if isinstance(other, ChessPlayer):
            return True if self.rating == other.rating else False
        return "Невозможно выполнить сравнение"
    
    def __gt__(self,other):
        if isinstance(other, int):
            return True if self.rating > other else False
        if isinstance(other, ChessPlayer):
            return True if self.rating > other.rating else False
        return "Невозможно выполнить сравнение"
    
    def __lt__(self,other):
        if isinstance(other, int):
            return True if self.rating < other else False
        if isinstance(other, ChessPlayer):
            return True if self.rating < other.rating else False
        return "Невозможно выполнить сравнение"


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(False, magnus == 4000) # False
print(True, ian == 2789) # True
print(False, magnus == ian) # False
print(True, magnus > ian) # True
print(False, magnus < ian) # False
print("Невозможно выполнить сравнениe", magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"
