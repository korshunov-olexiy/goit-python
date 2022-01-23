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
    arr = Manager().list()
    dict_sync = {}
    for number in numbers:
        dict_sync[number] = Process(target=factorize, args=(number, arr))
        dict_sync[number].start()
    while not all([not process.is_alive() for process in dict_sync.values()]):
        """"""
    return arr


@timebudget
def factorize_pool_proc(numbers: List[int]):
    arr = Manager().list()
    data = [[num, arr] for num in numbers]
    Pool(processes=cpu_count()-1).starmap(factorize, data)
    return arr


if __name__ == '__main__':
    RESULT = []
    data = [128, 255, 99999, 1065106000]
    print(factorize(data))
    print(factorize_sync(data))
    print(factorize_proc(data))
    print(factorize_pool_proc(data))
