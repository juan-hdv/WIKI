# Python (programming language)
From Wikipedia, the free encyclopedia

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

Using [Django](/wiki/Django) is it possible to develop web sites with javascritpt, [HTML](/wiki/HTML) and [CSS](/wiki/CSS).

## Python programming examples

Some simple code:

### Hello world program:

```
print('Hello, world!')
```

### Program to calculate the factorial of a positive integer:

```
n = int(input('Type a number, and its factorial will be printed: '))
if n < 0:
    raise ValueError('You must enter a non negative integer')
fact = 1
for i in range(2, n + 1):
    fact *= i
print(fact)
```