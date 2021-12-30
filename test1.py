from typing import Any


def decorator_class(cls):
    class NewClass:
        def __init__(self, *args, **kwargs) -> None:
            self._obj = cls(*args, **kwargs)
        def __getattribute__(self, __name: str) -> Any:
            attr = self._obj.__getattribute__(self, __name)
            print(attr)
            #if isinstance(__name, type(__name.__init__)):
            #    print("callable")
    return NewClass


@decorator_class
def func(a):
    print(f"test {a}")

f = func(3)
