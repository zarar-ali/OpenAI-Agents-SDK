from typing import Callable
from dataclasses import dataclass

# A callable that takes two integers and returns a string
MyFuncType = Callable[[int, int], str]

print(MyFuncType)

# Usage

@dataclass
class Calculator:
    operation: Callable[[int, int], str]

    def __call__(self, a: int, b: int) -> str:
        return self.operation(a, b)

def add_and_stringify(x: int, y: int) -> str:
    return str(x + y)

calc = Calculator(operation=add_and_stringify)

print(calc(5, 12))  # Outputs: '12'