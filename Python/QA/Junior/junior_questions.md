Junior questions python:
======

Q: What is Python?  
A: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

Q: What is the lambda function in Python? Why does it exist in Python?  
A: Lambda Function in Python is an anonymous function or a function having no name. Lambda functions behave just 
like regular functions declared with the def keyword. They can be used whenever function objects are required.

Q: What is `pass` in Python?  
A: The `pass` statement is a null statement. The pass statement is generally used as a placeholder

Q: What is `*args, **kwargs` in function definition?  
A: `*args` and `**kwargs` allow you to pass an unspecified number of arguments to a function.
`*args` - arguments (lists, tuples) and `**kwargs` - keywords arguments (dicts).

Q: What is docstring in Python? How to write them? Are they required?  
A: '''docs''' and """docs""" - right definition of docstring. Python documentation strings (or docstrings) 
provide a convenient way of associating documentation with Python modules, functions, classes, and methods. 
Docstring not a comments, docstring and # doc is not the same.

Q: What are the built-in data types that Python provides? Which of them are mutable, which are immutable?  
A: 

Q: What is the difference between list and tuple types in Python?  
A: list is mutable, whereas a tuple is immutable. This means that lists can be changed, and tuples cannot be changed.
Tuples are allocated large blocks of memory with lower overhead, since they are immutable; whereas for lists, 
small memory blocks are allocated. Between the two, tuples have smaller memory. This helps in making tuples faster than
lists when there are a large number of elements.

Q: What keywords can be used in conjunction with the `for` keyword?  
A: `for` can be used with `in` keyword. For example:
```python
for i in range(20):
    print(i)
```

Q: What could be the key in dict?  
A: Dictionary key must be of a type that is immutable. For ex.: integer, float, string, or Boolean as a dictionary key.
Either we can use all hashable types such as tuples, because they are immutable too. Lists, dicts and sets cant be as a keys,
because they are mutable.

Q: What's the difference between `globals()`, `locals()`, and `vars()`?  
A: 

Q: What is PEP8?  
A: PEP 8, sometimes spelled PEP8 or PEP-8, 
is a document that provides guidelines and best practices on how to write Python code.
For ex. max 79-character length for each line in code, naming conventions etc.
The primary focus of PEP 8 is to improve the readability and consistency of Python code.

Q: What is slicing in Python?  
A: Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists.
```python
a = 'string'
print(a[1:3]) # tr

b = [1, 3, 5, 6, 7, 3, 7, 4]
print(b[3:])  # [6, 7, 3, 7, 4]
print(b[2])  # 5
print(b[-5])  # 6
b[1] = "changed"
print(b)  # [1, 'changed', 5, 6, 7, 3, 7, 4]

# BUT IN STRING CANNOT CHANGE CHAR.
a[2] = 't'  # TypeError: 'str' object does not support item assignment

# For changing char we can do this for ex.:
c = a[:2] + 't' + a[3:]  #it's a string concatenation
print(c)  # stting
# or like this:
d = f'{a[:2]}t{a[3:]}' # it's a f-string
print(d)  # stting

```

Q: Is it possible to have a negative index in iterative types in Python?  
A: Yes, it is. We can get element for ex. from list by reverse way:
```python
b = [1, 3, 5, 6, 7, 3, 7, 4]
print(b[-2])  # 7
print(b[-5:-1])  # [6, 7, 3, 7]
print(b[2:-3])  # [5, 6, 7]
```

Q: What is the `__init__.py` module? What it's for?  
A: The `__init__.py` file lets the Python interpreter know that a directory contains code for a Python module.
An `__init__.py` file can be blank. Without one, you cannot import modules from another folder into your project.

Q: How can I swap values of variables in Python?  
A: 
```python
a = 1
b = 2

a, b = b, a

print('a = ', a)  # a =  2
print('b = ', b)  # b =  1

l = [0, 1, 2, 3, 4]

l[0], l[3] = l[3], l[0]

print(l)  # [3, 1, 2, 0, 4]
```

Q: How do I view object methods?  
A: The simplest way to get a list of methods of any object is to use the `help()` command.
The most useful way to get a list of methods of any object is to use the `dir()` command.
```python
# for python classes and objects 
print(help(str))
# or
print(dir(str))

# for handwrite classes

class MoreMethod(object):

    def some_method(self, x):
        return x

    def __getattr__(self, *args):
        return lambda x: x*2


print(help(MoreMethod))
# or
print(dir(MoreMethod))

```

Q: How do you get documentation on objects' methods in Python?  
A: `dir()`

Q: What is a module in python? What is a package? What is the difference between packages and modules in Python?  
A: The module is a simple Python file that contains collections of functions and global variables 
and with having a `.py` extension file. Package is a directory of 
Python modules containing an additional `__init__.py` file.

Q: Can you write multithreading applications in Python? What is the difference between multithreading and 
multiprocessing?  
A: Both multithreading and multiprocessing allow Python code to run concurrently. 
Only multiprocessing will allow your code to be truly parallel.  
The threading module uses threads, the multiprocessing module uses processes. 
The difference is that threads run in the same memory space, while processes have separate memory.
This makes it a bit harder to share objects between processes with multiprocessing.

Q: What is a decorator? How to create a custom decorator?  
A: A decorator is a design pattern in Python that allows a user to add new functionality 
to an existing object without modifying its structure.  
The decoration occurrs in the line before the function header. The "@" is followed by the decorator function name. 
All in all, we can say that a decorator is a callable object that is used to modify a function, method or class definition.

Q: What is `@classmethod`, `@staticmethod`, `@property`?  
A:
```python
class StudentC(object):
    """classmethod"""
    
    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_json(cls, json_obj):
        # parse json...
        return student

    @classmethod
    def from_pickle(cls, pickle_file):
        # load pickle file...
        return student


class StudentS(object):
    """staticmethod"""
    
    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

StudentS.is_full_name('Scott Robinson')   # True
StudentS.is_full_name('Scott')            # False


class Celsius:
    """property"""
    
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)  # Setting value...
print(human.temperature)  # Getting value... 37
print(human.to_fahrenheit())  # Getting value... 98.60000000000001
coldest_thing = Celsius(-300)  # Setting value...   ValueError: Temperature below -273 is not possible
```

Q: What is the difference between `@classmethod` and `@staticmethod`?  
A: A class method takes cls as the first parameter while a static method needs no specific parameters. 
A class method can access or modify the class state while a static method can't access or modify it. 
In general, static methods know nothing about the class state.

Q: Does Python fully support OOP?  
A: Python supports all the concept of "object oriented programming" but it is NOT fully object oriented because - 
The code in Python can also be written without creating classes.

Q: What is the `__dict__` attribute of an object in Python?  
A: save/represent all attributes of object in key-value format. 
```python
class Cat:

    def __init__(self, legs, colour):
        self.colour = colour
        self.legs = legs

figo = Cat(4, "GREEN")
print(figo.__dict__)  # {'colour': 'GREEN', 'legs': 4}
```

Q: What the `self` keyword is used for in Python?  
A:self represents the instance of the class. 
By using the “self” keyword we can access the attributes and methods of the class in python. 
It binds the attributes with the given arguments.

Q: What is the `__init__` function used for?  
A: The `__init__` function is called a constructor, or initializer, 
and is automatically called when you create a new instance of a class.
```python
class Dog:
    def __init__(self, legs, colour):
        self.legs = legs
        self.colour = colour

fido = Dog(4, "brown")
spot = Dog(3, "mostly yellow")
print(spot.__dict__)  # {'legs': 3, 'colour': 'mostly yellow'}
print(fido.__dict__)  # {'legs': 4, 'colour': 'brown'}
```

Q: What is pickling and unpickling(marshaling and unmarshaling)?  
A: “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and 
“unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) 
is converted back into an object hierarchy.  
Marshalling or marshaling (US spelling) is the process of transforming the memory representation of an object 
into a data format suitable for storage or transmission. The inverse process of marshalling is called 
unmarshalling (or demarshalling, similar to deserialization).


Coding questions:
------

Q: Write a function that produces the Fibonacci sequence.  
A: [1 answer](1_fibonacci.py)

Q: How to translate a string containing a binary code (1 and 0) into a number (integer)? Write a function to do this.  
A: [2 answer](2_binary.py)

Q: How to check that tuple A contains all elements of tuple B. Do both tuples contain unique values? 
Write a function to do this.  
A: [3 answer](3_tuples.py)

Q: What is the output of the following code?  
```python
def f():
    x = 15
    print(x)
x = 12
f()
```
A: `15`

Q: How to convert a string to a number that consists of letters ASCII code. Example: `'abcd' -> 979899100`. 
Write a function to do this.  
A: [5 answer](5_ascii.py)

Q: How to remove empty lines from a list of lines (with a length of 0). Write a function to do this.  
A: [6 answer](6_empty_deleter.py)

Q: Write a function that counts all distinct pairs with a difference equal to k.  
A: [7 answer](7_distinct.py)

Q: Write a function that returns a string of numbers from 0 to 100, `"0123456789101112..."`.  
A: [8_answer](8_num_str.py)

Q: Write a function that makes a list with unique items from a list with duplicate items. 
Example: `[1, 1, 2, 3, 3] -> [1, 2, 3]`  
A: [9_answer](9_unique_list.py)

Q: Make a list of prime numbers from the range (1, 100) using Python.  
A: [10_answer](10_list_primes.py)

Q: Write a program that prints the numbers from 1 to 20. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers that are multiples of both three and five print “FizzBuzz”.  
A: [11_answer](11_fizzbuzz.py)
