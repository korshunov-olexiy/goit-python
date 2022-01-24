from multiprocessing import Process, Manager, managers, Pool, cpu_count
from threading import Thread
from typing import List, Type
from timebudget import timebudget


class SyncThread(Thread):

    def __init__(self, wrapper: Type[object], num: int) -> None:
        self.wrapper = wrapper
        self.num = num
        super().__init__()

    def run(self):
        self.wrapper(self.num)


def factorize(numbers: List[int], array: Type[managers.ListProxy] = None):
    global RESULT
    if array is None:
        for number in numbers:
            RESULT.append([n for n in range(1, number+1)  if not number % n])
        return RESULT
    else:
        array.append([n for n in range(1, numbers+1)  if not numbers % n])


@timebudget
def factorize_sync(numbers: List[int]):
    dict_sync = {}
    global RESULT
    RESULT = []
    for number in numbers:
        dict_sync[number] = SyncThread(factorize, (number,))
        dict_sync[number].start()
    while not all([not res.is_alive() for res in dict_sync.values()]):
        """"""
    return RESULT


@timebudget
def factorize_proc(numbers: List[int]):
    res = []
    with Manager() as manager:
        arr = manager.list()
        dict_sync = {}
        for number in numbers:
            dict_sync[number] = Process(target=factorize, args=(number, arr))
            dict_sync[number].start()
        while not all([not process.is_alive() for process in dict_sync.values()]):
            """"""
        res = [a for a in arr]
    return res


@timebudget
def factorize_pool_proc(numbers: List[int]):
    res = []
    with Manager() as manager:
        arr = manager.list()
        data = [[num, arr] for num in numbers]
        Pool(processes=cpu_count()-1).starmap(factorize, data)
        res = [a for a in arr]
    return res


if __name__ == '__main__':
    RESULT = []
    data = [128, 255, 99999, 10651060]
    functions = [factorize, factorize_sync, factorize_proc, factorize_pool_proc]
    # Checking and displaying the result.
    for func in functions:
        a, b, c, d = func(data)
        print(a, b, c, d)
        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    