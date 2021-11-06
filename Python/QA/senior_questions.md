Senior questions python:
======

Q: Python always called an easy language. Will you agree with it?  
A: Yes, becouse:
Consider Hello World program in C,JAVA and PYTHON  
C CODE
```
#include <stdio.h> 
int main() 
{ 
 
   printf("Hello, World!"); 
   return 0; 
}
```
JAVA CODE
```javascript
public class HelloWorld { 
 
    public static void main(String[] args) { 
      
        System.out.println("Hello, World"); 
    } 
 
} 
```
PYTHON CODE
```python
print("Hello, World")
```

The major difference between all three is syntax and Python is easy to understand compared to other languages.

Q: What are the pitfalls and problems of Python language?  
A: GIL of course)))))))

Q: Is it possible to use the construction `True = False`?  
A: No, Only in python 2.x.

Q: When will the `else` part of `try...except...else` be executed?  
A: The else part is executed when no exception occurs.

Q: What is monkey patching? How to use it in Python? Example? Is it ever a good idea?  
A: [link for learn about](https://stackoverflow.com/questions/5626193/what-is-monkey-patching)

Q: How are dict and set implemented internally? What is the complexity of retrieving an item? How much memory 
do these structures consume?  
A: 

Q: Does Python support multiple inheritance? How does it solve the diamond problem?  
A: A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

In multiple inheritance, the features of all the base classes are inherited into the derived class. 
The syntax for multiple inheritance is similar to single inheritance.
````python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
````
In Python as all classes inherit from object, potentially multiple copies of object are inherited whenever multiple 
inheritance is used. That is, the diamond problem occurs even in the simplest of multiple inheritance.

Q: What is MRO in Python? How does it work?  
A: [guide](https://www.educative.io/edpresso/what-is-mro-in-python)

Q: Does Python has an assignment operator? How is the assignment process in Python different from C/C++?  
A: `+=`, `-=`, `*=`, `/=` - assignment operators in Python. Difference between C/C++ and Python is that 
assignment operator in C/C++ is `++`. [stackoverflow](https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python)

Q: What are descriptors? Is there a difference between a descriptor and a decorator?  
A: [guide](https://pythonguide.readthedocs.io/en/latest/python/decorator.html)

Q: How are arguments passed to function in Python — by value or by reference?  
A: Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object Reference" or "Call by Sharing"
If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like Call-by-value. 
It's different, if we pass mutable arguments. All parameters (arguments) in the Python language are passed by reference. 
It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.
[guide](https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/) 

Q: What tools help you find code smells in code or perform static code analysis? What else do you know/use to make your 
code maintainable and readable?  
A: flake8, black

Q: Whenever Python exits, why isn't all the memory de-allocated?  
A: When Python exit, the object referenced from global namespaces of Python modules are not always deallocated. 
So, Python doesn't recognize and free circular memory references before using the garbage collector.
[guide](https://www.i2tutorials.com/whenever-python-exists-why-isnt-all-the-memory-de-allocated/#:~:text=When%20Python%20exit%2C%20the%20object,before%20using%20the%20garbage%20collector.)

Q: Is it possible to have a producer thread reading from the network and a consumer thread writing to a file, really 
work in parallel? What about GIL?  
A: --//--

Q: What is GIL? Why GIL still exists?  
A: The GIL is a single lock on the interpreter itself which adds a rule that execution 
of any Python bytecode requires acquiring the interpreter lock. 
This prevents deadlocks (as there is only one lock) and doesn't introduce much performance overhead. 
But it effectively makes any CPU-bound Python program single-threaded.
Main reason why GIL still exists: The GIL prevents race conditions and ensures thread safety.

Q: What is string interning?  
A: The string interning in Python is a mechanism of storing only one copy of a string value in the memory. 
If there are a few string variables whose values are the same, they will be interned by Python implicitly and 
refer to the same object in the memory.

Q: Why Python doesn't have a tail recursion optimization? How to implement it?  
A: [link](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion)

Q: What is the process of compilation and linking in Python?  
A: __Compilation:__ The source code in python is saved as a .py file which is then compiled into a format known as byte code,
byte code is then converted to machine code. After the compilation, 
the code is stored in .pyc files and is regenerated when the source is updated. 
This process is known as compilation.

__Linking:__ Linking is the final phase where all the functions are linked with their definitions as the linker knows 
where all these functions are implemented. This process is known as linking.

__Example:__
````python
import dis
def recursive_sum(n):
    """Function to return the sum of recursive numbers"""
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)

# change this value for a different result
number = 16
if number < 0:
    print("The sum is",recursive_sum(number))
# by using dis module ,the bytecode is loaded into machine code ,and a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated.
dis.dis(recursive_sum)
````
__Output:__
```python
4           0 LOAD_FAST                0 (n)
              2 LOAD_CONST               1 (1)
              4 COMPARE_OP               1 (<=)
              6 POP_JUMP_IF_FALSE       12

  5           8 LOAD_FAST                0 (n)
             10 RETURN_VALUE

  7     >>   12 LOAD_FAST                0 (n)
             14 LOAD_GLOBAL              0 (recursive_sum)
             16 LOAD_FAST                0 (n)
             18 LOAD_CONST               1 (1)
             20 BINARY_SUBTRACT
             22 CALL_FUNCTION            1
             24 BINARY_ADD
             26 RETURN_VALUE
             28 LOAD_CONST               2 (None)
             30 RETURN_VALUE
```

Q: How to distribute Python code?  
A: The normal way of distributing Python applications is with distutils. 
It's made both for distributing library type python modules, 
and python applications, although I don't know how it works on Windows. 
You would on Windows have to install Python separately if you use distutils, in any case.
[link](https://packaging.python.org/overview/)

Q: How to package code in Python?  
A: [link_1](https://www.geeksforgeeks.org/packaging-and-publishing-python-code/)
[link_2](https://packaging.python.org/overview/)

Q: What is a package manager? What package managers do you know and which one do you recommend?  
A: pip is the de facto package manager in the Python world. It can install packages from many sources, 
but PyPI is the primary package source where it's used. When installing packages, 
pip will first resolve the dependencies, check if they are already installed on the system, and, if not, install them.
ALSO EXISTS: pip-tools, Poetry(10/10), Conda(Anaconda, it's the same.)

Q: How to work with Python transitive dependencies?  
A: [EVERYTHING ABOUT DEPENDENCIES](https://www.activestate.com/resources/quick-reads/python-dependencies-everything-you-need-to-know/)

Q: What are the wheels and eggs? What is the difference?  
A: Wheel and Egg are both packaging formats that aim to support the use case of needing an install artifact 
that doesn’t require building or compilation, which can be costly in testing and production workflows.
[Differences](https://packaging.python.org/discussions/wheel-vs-egg/)

Q: How to package binary dependencies in Python?  
A: Binary distributions are a subset of built distributions that contain compiled extensions. 
Extensions are non-Python dependencies or components of your Python package.
[link](https://www.activestate.com/resources/quick-reads/how-to-package-python-dependencies-for-publication/)

Q: What is Cython? What is IronPython? What is PyPy? Why do they still exist?  
A: [link](https://www.toptal.com/python/pochemu-sushchestvuet-tak-mnogo-pitonov)

Q: Explain how can you access a module written in Python from C? Vise versa?  
A: [link](https://docs.python.org/3/extending/extending.html)

Q: What is `__pycache__`? What are .pyc files?  
A: `__pycache__` is a directory that contains bytecode cache files that are automatically generated by python, 
namely compiled python, or . pyc , files.  
.pyc files are created by the Python interpreter when a .py file is imported. 
They contain the "compiled bytecode" of the imported module/program so that the "translation" 
from source code to bytecode (which only needs to be done once) can be skipped on subsequent 
imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. 
But it's still interpreted. Once the *.pyc file is generated, there is no need of *.py file, 
unless you edit it.

Q: How to speed up existing Python code? How would you speed up your, say, web app?  
A: [speed up code](https://www.kdnuggets.com/2021/06/make-python-code-run-incredibly-fast.html)  
speed up web: cache(redis for ex.), asynchronous code, microservices, message queue and etc...

Q: How to isolate Python code? What are virtualenvs?  
A: Virtual environments, or "virtualenvs" are lightweight, self-contained Python installations, 
designed to be set up with a minimum of fuss, and to "just work" without requiring extensive 
configuration or specialized knowledge. virtualenv avoids the need to install Python packages globally.
PRO LEVEL: to use a docker/kubernetes containers.

Q: Is Python a functional language? Specify the requirements for code written in a functional paradigm.  
A: Although Python is not primarily a functional language, 
it's good to be familiar with `lambda` , `map()` , `filter()` , and `reduce()` because they can help you write concise, 
high-level, parallelizable code.

Q: Identify the pitfalls/limitations of the functional code.  
A: [link](https://stackoverflow.com/questions/1786969/pitfalls-disadvantages-of-functional-programming)

Q: What are .pth files?  
A: PTH is a data file for Machine Learning with PyTorch. (with weights and other needful data)

Q: What advantages do NumPy arrays offer over (nested) Python lists?  
A: [link](https://www.quora.com/What-advantages-do-NumPy-arrays-offer-over-nested-Python-lists)

Q: What does the `PYTHONOPTIMIZE` flag do?  
A: [link](https://stackoverflow.com/questions/2830358/what-are-the-implications-of-running-python-with-the-optimize-flag#:~:text=When%20the%20Python%20interpreter%20is,%2C%20all%20bytecode%20is%20optimized%3B%20.)

Q: You have a memory leak in the working production application on one of your company servers. 
How would you start debugging it?  
A: --//--


Coding questions:
------

Q: Give an example of a filter and reduce over an iterable object.  
A: 

Q: Write a function that reverses the generator?  
A: [2_answer](Senior/2_reverse_generator.py)

Q: You need to implement a function that should use a static variable (for example, a call counter). 
You cannot write any code outside the function and you do not have information about external variables 
(outside your function). How to do it?  
A: 

Q: What methods and in what order are called when print `(A() + B())` is executed?  
A: 

Q: How to implement a dictionary from scratch using core Python?  
A: 

Q: What's the output?  
```python
def Foo(): 
    yield 42;
    return 666
```
A: `42  # because it's a generator (doesn't return 666)`

Q: What will be the output of the following code?  
```python
a = [[]] * 3
a[1].append(1)
print(a)  # [[1], [1], [1]
```
A: `[[1], [1], [1]`

Q: Place the following functions below in order of their efficiency. How would you test your answer?  
```python
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
```
A: [9_answer](Senior/9_O_big.py)

Q: Write a one-liner that will count the number of capital letters in a file. 
Your code should work even if the file is too big to fit in memory.  
A: 

Q: What will be the output of the following code? Why? Is this inheritance?  
```python
class C:
    pass

type (C())
type (C)
```
A: First will be instance of class C, second one will be instance of type cause inheritance.
```python
<class '__main__.C'>
<class 'type'>
```

Q: What will be the output of the following code?  
```python
big_num_1 = 1000
big_num_2 = 1000
small_num_1 = 1
small_num_2 = 1
big_num_1 is big_num_2
small_num_1 is small_num_2
```
A: I DONT KNOW WHY
```python
True
True
```

Q: How is this possible?  
```python
_MangledGlobal__mangled = 23

class MangledGlobal:
     def test(self):
         return __mangled

print(MangledGlobal().test())  # 23
```

A: problems with naming in python.  
In this example I declared a global variable called `_MangledGlobal__mangled`. Then I accessed the variable inside the 
context of a class named `MangledGlobal`. Because of name mangling I was able to reference the `_MangledGlobal__mangled` 
global variable as just `__mangled` inside the `test()` method on the class.

The Python interpreter automatically expanded the name `__mangled` to `_MangledGlobal__mangled` because it begins with 
two underscore characters. This demonstrated that name mangling isn’t tied to class attributes specifically. 
It applies to any name starting with two underscore characters used in a class context.

Q: What will be the output of the following code?  
```python
print(_)
```
A: `NameError: name '_' is not defined`

Q: You saw the following piece of code. What is wrong with this code? Why is it needed?  
```python
if __debug__:
    assert False, ("error")
```
A: `AssertionError: error`
