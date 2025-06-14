# Type variable for generic typing
from typing import TypeVar, Any

"""
# Generics in Python

Generics allow us to define functions and classes that can operate on different data types while maintaining type safety.

# 1. Introduction to Generics
---------------------------

Issues
-> Any: I don't know the data type.
-> We have by
"""

# Example without Generics

fruits = ["mango", "apple"]

def first_element(items: list[Any]) -> Any:
    """
    Takes a list...

    Args:
      items: A list of items.

    Returns:
      The first item in the list.
    """
    return items[0]


# Infer : def first_element(items: list[T]) -> T:
# -> 1. I will pass a list where all items will have same type
# -> 2. <T> is fill in the blank. <T> will be whatever type we define
# -> 3. Whatever type of <T> is will be returned.

nums = [1, 2, 3]
strings = ['a', 'b', 'c']

print(first_element(nums))     # 1
print(first_element(strings))  # 'a'


"""# 2. Using Generics
------------------

Generics let you create functions, methods, or classes that can work with multiple types while preserving type relationships. Generics:

- Better communicate the intent of your code.
- Allow static type checking to verify correctness.

In Python, this is done using TypeVar.

🔹 Using TypeVar
First, import TypeVar and define a generic type variable T:

```python
from typing import TypeVar

T = TypeVar("T")  # T represents a generic type
```

- `T` is a placeholder that can be **replaced with any type** when the function is called.
- The **actual type is inferred at runtime**.
"""


nums = [1, 2, 3]
strings = ['a', 'b', 'c']

# Analogy -> Think of T as fill in the Blank
# -> using T is community driven practice.
T = TypeVar('T')

def generic_first_element(items: list[T]) -> T:
    return items[0]

num_result = generic_first_element(nums)        # type inferred as int
string_result = generic_first_element(strings)  # type inferred as str

print(num_result)    # 1
print(string_result) # 'a'

"""#### Why Use Generics When Python Lets You Pass Any List?

Explanation: By using Generics, Python can infer and enforce types at compile-time, enhancing clarity and safety.

1. **Static Type Checking**  
   - **Without generics**, you can pass any list, but static type checkers (like [mypy](http://mypy-lang.org/)) cannot verify that your function is used correctly. For instance, if your function is meant to handle only strings but you accidentally pass a list of integers, Python won't complain until (or unless) something goes wrong at runtime.  
   - **With generics**, you declare something like `List[str]` or `List[int]`, and a type checker will immediately flag if you pass the wrong type. This early feedback catches type errors before they become runtime bugs.

2. **Code Clarity and Intent**  
   - Generics communicate clearly to other developers (and future you) that `first_element(items: List[T]) -> T` is intended to work with a list of a single, consistent type `T`.  
   - When you see `List[str]`, there is no ambiguity about what the list is supposed to contain. This helps prevent accidental mixing of data types.

3. **Improved Tooling Support**  
   - Modern IDEs can use your generic annotations to provide better **autocompletion, refactoring,** and **linting** suggestions.  
   - For example, if a function returns `T`, your IDE will automatically know the returned type is `str` for a `List[str]`, saving time when using the result elsewhere in your code.

4. **Future-Proofing**  
   - As projects grow more complex and data structures become nested, generics help keep track of types. This is especially crucial in large-scale applications like **production AI systems**, where data consistency and correctness are paramount.

5. **Avoiding Silent Logic Errors**  
   - Without generics, a developer could pass any list, perhaps by mistake. You might not catch it until it causes a subtle bug (like a `TypeError` in production).  
   - By declaring generic types, the mismatch is caught early, which often saves hours of debugging.

---

In short, Python’s flexibility of “pass any list” is convenient for small scripts or quick prototypes. However, in larger, more complex, or production-grade systems—especially with AI or data-heavy workflows—generics, combined with type checkers, dramatically improve reliability, clarity, and maintainability.
"""
# <=============================== Generic Classes =======================================>

"""# 3. Generic Classes
------------------

Generics can also be used with classes.

"""

from typing import Generic, TypeVar, ClassVar
from dataclasses import dataclass, field

# Type variable for generic typing
T = TypeVar('T')

@dataclass
class Stack(Generic[T]):
    # Instance Level -> obj = Stack
    items: list[T] = field(default_factory=list)
    # Class Level ->
    limit: ClassVar[int] = 10

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Infer
# 1. On seeing T i assumed there will be generic types.
# 2. T is an unknown/ fill in the blank type. We will get type in runtime.

stack_of_ints = Stack[int]()
print(stack_of_ints)

print(stack_of_ints)
print(stack_of_ints.limit)


stack_of_ints.push(10)
stack_of_ints.push(20)

print(stack_of_ints.pop())  # 20


stack_of_strings = Stack[str]()
print(stack_of_strings)

stack_of_strings.push("hello")
stack_of_strings.push("world")

print(stack_of_strings.pop())  # 'world'

print(Stack.limit)
print(stack_of_ints.limit)