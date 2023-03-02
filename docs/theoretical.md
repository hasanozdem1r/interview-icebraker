# Python Theoretical Questions

Theoretical interview questions in Python are designed to assess a candidate's understanding of fundamental concepts and principles in the field of software development. 

### 1. What are key features of Python ?

* Easy to learn due to clear syntax and readability	
* Easy to interpret, making debug is easy
* Free and open source
* OOP supported, general purpose programming language
* Python is **dynamically typed**, this means that you don’t need to state the types of variables when you declare them or anything like that.

### 2. What are keywords in Python ?

Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier.
Here's a list of all keywords in Python Programming

![Keywords](img/theoretical/keywords.PNG)

### 3. What are literals in Python ?

Literals in Python refer to the data that is given in a variable or constant. 

* String Literals
* Numeric Literals
* Boolean Literals
* Special Literals

### 4. What are functions in Python ?
Functions in Python refer to blocks that have organised, and reusable codes to perform single, and related events. Functions are important to create better modularity for applications which reuse high degree of coding. Functions are executed only when a call is made to the function.

### 5. What is the difference between list and tuples in Python ?

| **LIST**                          | **TUPLE**                             |
|-------------------------------	|------------------------------------	|
| Mutable. Items can be changed 	| Immutable. Items cannot be changed 	|
| Slower than tuples            	| Faster than list                   	|
| eg_list= [1,2,3,4,5]          	| example=(1,2,3,4,5)                	|

### 6. What are Python namespaces ?
A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.The objects are variables and functions. 

* Built-in namespace– These namespaces contain all the built in objects in python and are available whenever python is running.
* Global namespace– These are namespaces for all the objects created at the level of the main program.
* Enclosing namespaces– These namespaces are at the higher level or outer function.
* Local namespaces– These namespaces are at the local or inner function.

### 7. What are decorators in Python ? 
Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. Decorators are used to add some design patterns to a function without changing its structure. 

Decorators generally are defined before the function they are enhancing. To apply a decorator we first define the decorator function. Then we write the function it is applied to and simply add the decorator function above the function it has to be applied to. For this, we use the **@ symbol** before the decorator.

```
def whee_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@whee_decorator
def say_whee():
    print("Whee!")
```

### 8. What is slicing in Python ?
Slicing is used to access parts of sequences like lists, tuples, and strings.

The syntax of slicing is  `[start:stop:step]`

* **start**: refer starting index for collection. In Python first index is 0
* **stop**: refer last index for collection which is not included.
* **step**: refer incrementation / decrementation for each iteration.

Checkout following examples to understand better
```
example=[]
example[start:stop]  # items start through stop-1
example[start:]      # items start through the rest of the array
example[:stop]       # items from the beginning through stop-1
example[:]           # a copy of the whole array
example[start:stop:step] # # start through not past stop, by step
```

### 9. How is memory managed in Python ?
Memory is managed in Python in the following ways:
1.	Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a **private heap**. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
2.	The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
3.	Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

### 10. What are python modules? Name some commonly used built-in modules in Python ?
A module is a file containing Python definitions and statements. This code can either be functions classes or variables. Ex ; os, sys, math, random, JSON, csv