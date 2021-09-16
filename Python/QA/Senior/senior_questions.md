Q: Python always called an easy language. Will you agree with it?
A:
Q: What are the pitfalls and problems of Python language?
A:
Q: Is it possible to use the construction True = False?
A:
Q: When will the else part of try...except...else be executed?
A:
Q: What is monkey patching? How to use it in Python? Example? Is it ever a good idea?
A:
Q: How are dict and set implemented internally? What is the complexity of retrieving an item? How much memory do these structures consume?
A:
Q: Does Python support multiple inheritance? How does it solve the diamond problem?
A:
Q: What is MRO in Python? How does it work?
A:
Q: Does Python has an assignment operator? How is the assignment process in Python different from C/C++?
A:
Q: What are descriptors? Is there a difference between a descriptor and a decorator?
A:
Q: How are arguments passed to function in Python — by value or by reference?
A:
Q: What tools help you find code smells in code or perform static code analysis? What else do you know/use to make your code maintainable and readable?
A:
Q: Whenever Python exits, why isn't all the memory de-allocated?
A:
Q: Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really work in parallel? What about GIL?
A:
Q: What is GIL? Why GIL still exists?
A:
Q: What is string interning? Why it Python have it?
A:
Q: Why Python doesn't have a tail recursion optimization? How to implement it?
A:
Q: What is the process of compilation and linking in Python?
A:
Q: How to distribute Python code?
A:
Q: How to package code in Python?
A:
Q: What is a package manager? What package managers do you know and which one do you recommend?
A:
Q: How to work with Python transitive dependencies?
A:
Q: What are the wheels and eggs? What is the difference?
A:
Q: How to package binary dependencies in Python?
A:
Q: What is Cython? What is IronPython? What is PyPy? Why do they still exist?
A:
Q: Explain how can you access a module written in Python from C? Vise versa?
A:
Q: What is __pycache__? What are .pyc files?
A:
Q: How to speed up existing Python code? How would you speed up your, say, web app?
A:
Q: How to isolate Python code? What are virtualenvs?
A:
Q: Is Python a functional language? Specify the requirements for code written in a functional paradigm.
A:
Q: Identify the pitfalls/limitations of the functional code.
A:
Q: What are .pth files?
A:
Q: What advantages do NumPy arrays offer over (nested) Python lists?
A:
Q: What does the PYTHONOPTIMIZE flag do?
A:
Q: You have a memory leak in the working production application on one of your company servers. How would you start debugging it?
A:

Coding questions:
Q: Give an example of a filter and reduce over an iterable object.
A:
Q: Write a function that reverses the generator?
A:
Q: You need to implement a function that should use a static variable (for example, a call counter). You cannot write any code outside the function and you do not have information about external variables (outside your function). How to do it?
A:
Q: What methods and in what order are called when print (A() + B()) is executed?
A:
Q: How to implement a dictionary from scratch using core Python?
A:
Q: What's the output?

def Foo(): 
    yield 42;
    return 666

A:
Q: What will be the output of the following code?
>>> a = [[]] * 3
>>> a[1].append(1)
>>> print(a)  # [[1], [1], [1]

A:
Q: Place the following functions below in order of their efficiency. How would you test your answer?

def f1(arr):
    l1 = sorted(arr)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]
def f2(arr):
    l1 = [i for i in arr if i<0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]
def f3(arr):
    l1 = [i * i for i in arr]
    l2 = sorted(l1)
    return [i for i in l1 if i < (0.5*0.5)]

A:
Q: Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.
A:
Q: What will be the output of the following code? Why? Is this inheritance?

class C:
    pass

type (C())
type (C)

A:
Q: What will be the output of the following code?
big_num_1   = 1000
big_num_2   = 1000
small_num_1 = 1
small_num_2 = 1
big_num_1 is big_num_2
small_num_1 is small_num_2

A:
Q: How is this possible?

_MangledGlobal__mangled = 23

class MangledGlobal:
     def test(self):
         return __mangled

>>> MangledGlobal().test()
23

A:
Q: What will be the output of the following code?

>>> print(_)

A:
Q: You saw the following piece of code. What is wrong with this code? Why is it needed?

if __debug__:
    assert False, ("error")

A: