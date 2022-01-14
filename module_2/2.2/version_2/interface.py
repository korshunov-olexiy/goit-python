from abc import abstractmethod
from typing import List, Union

class Interface:
    """Base class for the data retrieval environment."""

    @abstractmethod
    def get_msg(self, console_text: str, type_return: Union[str, List[str]]) -> Union[str, List[str]]:
        """"""
