from abc import ABC, abstractclassmethod
from typing import Iterable

class Creator(ABC):

    @abstractclassmethod
    def create(self):
        """"""

    def output_data(self, *info) -> str:
        creator = self.create()
        result = creator.output(*info)
        return result


class SendData(ABC):

    @abstractclassmethod
    def output(self, *info) -> str:
        """"""


class CreatorCMD(Creator):
    def create(self) -> SendData:
        return SendDataCMD()


class SendDataCMD(SendData):

    def output(self, *info) -> str:
        print(*info)


def client_code(creator: Creator, *info: Iterable):
    return creator.output_data(*info)

cli = client_code(CreatorCMD(), "iterable object")
