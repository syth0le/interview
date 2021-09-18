Middle questions python:
======

Q: What is the output of -12 % 10?  
A: 8

Q: What is the output of -12 // 10?  
A: -2

Q: Why shouldn't you make the default arguments an empty list?  
A: cause in second function/method call it will refer to an already created object in memory.

Q: What `id()` function in Python is for?  
A: returns unique and permanent identificator for object

Q: What is the `yield` keyword used for in Python?  
A: returns a value without deleting local variables. Using in generators for example.

Q: What is an iterator in Python? Can you write an example?  
A: Iterator is an object that contains a countable number of values. Iterator is object which returns iterated values. 

Q: What is a generator in Python? How are they different from iterators?  
A: Generators is a subset of iterators. But it doesn't return its values after initialization.
We can create generator and use it in other place in code. Finally, generators use keyword: `yield`.

Q: What is the difference between `__iter__` and `__next__`?  
A: `__iter__` returns the iterator object itself and the `__next__` method returns the next value from the iterator

Q: How do you create a dictionary which can preserve the order of pairs?  
A: Ordered dict from collections.

Q: What is a context manager? How are they different from try ... finally?  
A: Context manager `with` (or `from contextlib import contextmanager` and using it as decorator for function/method) 
is a syntax sugar. [read about](https://medium.com/swlh/python-coding-tip-using-the-with-statement-instead-try-finally-f45a645c6008)

Q: Which functions must be overridden in a class in order for its instances to implement the context manager protocol?  
A: To implement a context manager, we define a class containing an `__enter__()` and `__exit__()` method

Q: What is the synchronous code? What is asynchronous code? How to write asynchronous code?  
A: Synchronous means to be in a sequence, i.e. every statement of the code gets executed one by one.  

Asynchronous coding often means that you need to multi-thread your code. 
This means that you have to start another thread that can run independently of your main task. 
This is often necessary because, as an example, waiting on communication 
to complete completely stops the thread that is waiting from running.



Q: What is unittest module in Python? How to write tests in Python?  
A: The unittest module provides a rich set of tools for constructing and running tests. 
[documentation](https://docs.python.org/2/library/unittest.html#).
````python
import unittest

from Car import Car


class TestCar(unittest.TestCase):
      def setUp(self):
          self.car = Car()


class TestInit(TestCar):
      def test_initial_speed(self):
          self.assertEqual(self.car.speed, 0)

      def test_initial_odometer(self):
          self.assertEqual(self.car.odometer, 0)

      def test_initial_time(self):
          self.assertEqual(self.car.time, 0)


class TestAccelerate(TestCar):
      def test_accelerate_from_zero(self):
          self.car.accelerate()
          self.assertEqual(self.car.speed, 5)

      def test_multiple_accelerates(self):
          for _ in range(3):
            self.car.accelerate()
          self.assertEqual(self.car.speed, 15)


class TestBrake(TestCar):
       def test_brake_once(self):
           self.car.accelerate()
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes(self):
            for _ in range(5):
                self.car.accelerate()
            for _ in range(3):
                self.car.brake()
            self.assertEqual(self.car.speed, 10)

       def test_should_not_allow_negative_speed(self):
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes_at_zero(self):
           for _ in range(3):
               self.car.brake()
           self.assertEqual(self.car.speed, 0)
````

Q: What is type checking? Why Python is a strongly typed language? Do we have types in Python?  
A: Type checking means checking that each operation should receive proper number of arguments and of proper data type.
 Python is strongly typed as the interpreter keeps track of all variables types. 
Python will always remain a dynamically typed language. 
However, PEP 484 introduced type hints, which make it possible to also do static type checking of Python code. 
Unlike how types work in most other statically typed languages, type hints by themselves don't cause Python to enforce types.


Q: How can you copy an object in Python? How to make a deep copy?  
A: use `=` operator to create a copy of an object. To make a deep copy (or clone) of an object, 
we import the built-in copy module in Python. This module has the deepcopy() method which simplifies our task.
````python
import copy

# Using '=' operator
x = [1, 2, 3]
y = x
x[0] = 5    # value of 'y' also changes as it is the SAME object
x[1] = 15
print("Shallow copy: ", y)  # Shallow copy:  [5, 15, 3]

# Using copy.deepcopy()
a = [10, 20, 30]
b = copy.deepcopy(a)
a[1] = 70   # value of 'b' does NOT change because it is ANOTHER object
print("Deep copy: ", b)  # Deep copy:  [10, 20, 30]

````

Q: How memory is managed in Python? Why garbage collector exists in Python?  
A: The Python memory manager manages chunks of memory called “Blocks”. 
A collection of blocks of the same size makes up the “Pool”. 
Pools are created on Arenas, chunks of 256kB memory allocated on heap=64 pools. 
If the objects get destroyed, the memory manager fills this space with a new object of the same size.
So, Python garbage collection algorithm is very useful to open up space in the memory.

Q: How the garbage collector works in Python? Describe Python's garbage collection mechanism in brief.  
A: The garbage collector is keeping track of all objects in memory. 
A new object starts its life in the first generation of the garbage collector. 
If Python executes a garbage collection process on a generation and an object survives, 
it moves up into a second, older generation.
Garbage collection is implemented in Python in two ways: reference counting and generational.
When the reference count of an object reaches 0, 
reference counting garbage collection algorithm cleans up the object immediately.

Q: How can you share global variables across modules? Is it a good idea to do that?  
A: Globals in Python are global to a module, not across all modules. 
If you need truly global variables from imported modules, you can set those at an attribute of the module where you're importing it.
The best way to share global variables across modules across a single program is to create a config module. 
Just import the config module in all modules of your application; the module then becomes available as a global name.

Q: What is the `__slots__` attribute used in a class for?  
A: Why use `__slots__` : Faster attribute access. 
Slots provide a special mechanism to reduce the size of objects.It is a concept of memory optimisation on objects.
Also object with slots can't set, get, give different attributes, which `__slots__` doesn't include.
````python
import timeit


class GFG(object):
    __slots__ = 'foo'


class Usual(object):
    pass


def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo
    return get_set_delete


if __name__ == "__main__":
    instance = GFG()
    instance_2 = Usual()
    instance_2.new = "new"
    print(instance_2.new)  # new
    instance.new = "new"
    print(instance.new)  # AttributeError: 'GFG' object has no attribute 'new'
    print(min(timeit.repeat(get_set_delete_fn(instance))))  # 0.1264069
    print(min(timeit.repeat(get_set_delete_fn(instance_2))))  # 0.16134380000000004
````

Q: What are metaclasses in Python?  
A: A metaclass in Python is a class of a class that defines how a class behaves. 
A class in Python defines how the instance of the class will behave. Custom metaclasses:
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

print(type(SingletonClass))  # <class '__main__.SingletonMeta'>
```


Q: How to create a class without a class statement?  
A: [link for learn about](https://www.datacamp.com/community/tutorials/python-metaclasses)


Coding questions:
------

Q: What will be the output of the following code?  
```python
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:]) # []
```

A: `[]`

Q: How can I reload a previously imported module? (we assume that the module is a file module.py)  
A: --//--

Q: What will be the output of the following code?  
```python
a = [[]]*3
a[1].append(1)
print(a)  # [[1], [1], [1]]
```
A: `[[1], [1], [1]]`

Q: What's wrong with the following code?  
```python
def foo():
    from .module import *
    print(f"{bar()}")
```
A: `SyntaxError: import * only allowed at module level`

Q: The file is located in /usr/lib/python/person.py. The program is run with python /usr/lib/python/person.py. 
What will the output be?  
```python
class Person:
    def __init__(self, name):
        __name__ = name

    def getAge(self):
        print(__name__)

p = Person("John")
p.getAge()
```
A: `__main__`

Q: Write a timeit decorator to measure the time of function execution.  
A: [6_answer](Middle/6_decorator_time.py)

Q: Write a decorator that will catch errors and repeat the function a maximum of 3 times (configurable).  
A: [7_answer](Middle/7_decorator_repeater.py)

Q: What's the output of the following code?  
```python
class parent:
    def __init__(self, param):
        self.v1 = param

class child:
    def __init__(self, param):
        self.v2 = param

obj = child(11)
print(obj.v1 + " " + obj.v2)
```
A: `AttributeError: 'child' object has no attribute 'v1'`

Q: Fix the following code to make it work.  
```python
class Repeater:
    ...
class RepeaterIterator:
    ...

repeater = Repeater("Hello")
for i in repeater:
    print(i)  # hello
```
A: [9_answer](Middle/9_repeater.py)

Q: Write code to get unique values from a list of complex types (custom classes). Example:  
```python
[A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab")] -> [A(1, "ab"), A(2, "ab"), A(2, "aa")]
```
A: [10_answer](Middle/10_unique_kwrgs.py)

Q: We have the following code with the unknown function `f()`. In `f()`, we do not want to use a return, instead, 
we may want to use a generator.  
```python
for x in f(5):
    print(x,)
```
The output looks like this:
```python
0 1 8 27 64
```
Write a function `f()` so that we can have the output above.  
A: [11_answer](Middle/11_unknown_func.py)

Q: What's the output of the following code?  
```python
x = [[0], [1]]
print(len(' '.join(list(map(str, x)))))
```
A: `7  # without len = [0] [1]`
