Middle questions python:
======

Q: What is the output of -12 % 10?  
A:

Q: What is the output of -12 // 10?  
A:

Q: What is the sequence of call operators in the expression a * b * c?  
A:

Q: Why shouldn't you make the default arguments an empty list?  
A:

Q: What id() function in Python is for?  
A:

Q: What is the yield keyword used for in Python?  
A:

Q: What is an iterator in Python? Can you write an example?  
A:

Q: What is a generator in Python? How are they different from iterators?  
A:

Q: What is the difference between __iter__ and __next__?  
A:

Q: How do you create a dictionary which can preserve the order of pairs?  
A:

Q: What is a context manager? How are they different from try ... finally?  
A:

Q: Which functions must be overridden in a class in order for its instances to implement the context manager protocol?  
A:

Q: What is the synchronous code? What is asynchronous code? How to write asynchronous code?  
A:

Q: What is unittest module in Python? How to write tests in Python?  
A:

Q: What is type checking? Why Python is a strongly typed language? Do we have types in Python?  
A:

Q: How can you copy an object in Python? How to make a deep copy?  
A:

Q: How memory is managed in Python? Why garbage collector exists in Python?  
A:

Q: How the garbage collector works in Python? Describe Python's garbage collection mechanism in brief.  
A:

Q: How can you share global variables across modules? Is it a good idea to do that?  
A:

Q: What is the __slots__ attribute used in a class for?  
A:

Q: What are metaclasses in Python?  
A:

Q: How to create a class without a class statement?  
A:


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
A: [6_answer](6_decorator_time.py)

Q: Write a decorator that will catch errors and repeat the function a maximum of 3 times (configurable).  
A: [7_answer](7_decorator_repeater.py)

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
A: [9_answer](9_repeater.py)

Q: Write code to get unique values from a list of complex types (custom classes). Example:  
```python
[A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab")] -> [A(1, "ab"), A(2, "ab"), A(2, "aa")]
```
A: [10_answer](10_unique_kwrgs.py)

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
Write a function f() so that we can have the output above.  
A: [11_answer](11_unknown_func.py)

Q: What's the output of the following code?  
```python
x = [[0], [1]]
print(len(' '.join(list(map(str, x)))))
```
A: `7  # without len = [0] [1]`
