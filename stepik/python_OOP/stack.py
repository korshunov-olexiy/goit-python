'''В этом задании вам предстоит реализовать свой стек(stack) -
это упорядоченная коллекция элементов, организованная по
принципу LIFO (англ. last in — first out,
"последним пришёл — первым вышел").'''

class Stack:
    def __init__(self):
        self.values = []
    def push(self,item):
        self.values.append(item)
    def pop(self):
        if not self.values:
            print("Empty Stack")
            return None
        return self.values.pop()
    def peek(self):
        if not self.values:
            print("Empty Stack")
            return None
        return self.values[-1]
    def is_empty(self):
        return False if self.values else True
    def size(self):
        return len(self.values)
