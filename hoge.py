from typing import Tuple


class MyClass:
    i = 12345

    def __init__(self):
        self.i = 23456

    def f(self, x):
        print("hello, " + x)

    def add(self, x: Tuple[int, int, str]):
        n1, n2, s = x
        print(f"{s}")
        return n1 + n2


x = MyClass()
x.f("kiyoshi")

print(f"add is {x.add((1,2, 'hoge'))}")
