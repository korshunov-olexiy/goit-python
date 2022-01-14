from typing import Union, List
from interface import *

class InterfaceCMD(Interface):
    """Console interface for getting values from the user."""

    def get_msg(self, console_text: str, type_return: Union[str, List[str]]) -> Union[str, List[str]]:
        """"""
        input_msg = input(f"{console_text}:\n").strip()
        if type_return == list:
            input_msg = input_msg.split(";")
        return input_msg
