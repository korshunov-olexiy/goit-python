from multiprocessing import Process
from threading import RLock, Thread
from time import sleep
from typing import Type
from sys import exit
from timebudget import timebudget


class SyncThread(Thread):

    def __init__(self, wrapper: Type[object], num: int) -> None:
        self.wrapper = wrapper
        self.num = num
        super().__init__()

    def run(self):
        self.wrapper(self.num)


@timebudget
def factorize(*number):
    result = []
    for num in number:
        result.append([n for n in range(1, num+1)  if not num % n])
    return result


@timebudget
def factorize_sync(*number):
    result = []

    def wr(num):
        result.append([n for n in range(1, num+1) if not num % n])
    dict_sync = {}
    for num in number:
        dict_sync[num] = SyncThread(wr, num)
        dict_sync[num].start()
    while not all([not res.is_alive() for res in dict_sync.values()]):
        """"""
    return result

def f(number):
    print([n for n in range(1, number+1)  if not number % n])
    exit(0)
    # return result

@timebudget
def factorize_proc(*number):
    result = []

    dict_sync = {}
    for num in number:
        dict_sync[num] = Process(target=f, args=(num,))
        dict_sync[num].start()
    while not all([not res.is_alive() for res in dict_sync.values()]):
        """"""
    return result



if __name__ == '__main__':
    # factorize(128, 255, 99999, 10651060)
    # print(factorize_sync(10651060, 128, 255, 99999))
    factorize_proc(128, 255, 99999, 10651060)
