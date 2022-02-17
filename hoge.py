from dataclasses import dataclass
from typing import Tuple

import logging

logging.basicConfig(
    format="%(asctime)s %(filename)s:%(lineno)4d [%(levelname)8s] %(message)s",
    encoding="utf-8",
    level=logging.DEBUG,
    filename="test.log"
)


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


@dataclass(frozen=True)
class MyClass2:
    name: str
    id: int

    def get_text(self) -> str:
        return f"{self.id}-{self.name}"


n = 123
logging.debug(f"hello {n}")
logging.info("hello")
logging.warning("hello")
logging.error("hello")

x: MyClass = MyClass()
x.f("kiyoshi")

print(f"add is {x.add((1,2, 'hoge'))}")

mc2 = MyClass2("nakahara", 123)
logging.debug(f"{mc2.get_text()}")
logging.debug(mc2)
# mc2.id=124 # dataclasses.FrozenInstanceError: cannot assign to field 'id'
