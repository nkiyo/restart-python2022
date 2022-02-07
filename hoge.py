from typing import Tuple


class MyClass:
    i: int = 12345

    def __init__(self):
        self.i = 23456

    def f(self, x: str) -> None:
        print("hello, " + x)

    def add(self, x: Tuple[int, int, str]) -> int:
        n1, n2, s = x
        print(f"{s}")
        return n1 + n2


x: MyClass = MyClass()
x.f("kiyoshi")

print(f"add is {x.add((1,2, 'hoge'))}")
