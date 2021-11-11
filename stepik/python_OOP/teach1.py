class AMD:
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class Intel:
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class CPU(AMD, Intel):
    def __init__(self, cls) -> None:
        print(cls)
        super().__init__()

class NVidia:
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class GeForce:
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class GPU(NVidia, GeForce):
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class Memory:
    def __init__(self, value) -> None:
        self.value = value
        super().__init__()

class Motherboard(CPU, GPU, Memory):
    def __init__(self, cpu:CPU, gpu:GPU, memory:Memory):
        super().__init__()
    def showinfo():
        pass


motherboard = Motherboard( \
    CPU(AMD('Raizen 12')), \
    GPU(NVidia('Radeon RX 6600 XT')), \
    Memory('SanDisk SDSDQL-032G 32GB Class 10'))
