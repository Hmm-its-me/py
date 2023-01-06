# Error can be a syntax error or an exception
# Most common builtin exceptions
# How can we raise and handle exceptions?
# How can we defien our own exceptions

# Even when a statement is syntactically correct, it may raise an
# Error when it is executed -> This is called an exception error;

# There are several error classes
"""Ex: 1. Type error
       2. import error
       3. name error
       4. FileNotFoundError
       5. ValueError
       6. IndexError
       7. KeyError
...etc"""

# Raising Exceptions
x = 5
if x < 0:
    raise Exception("x should be >= 0")
else:
    print(x)

x = 5
assert (x >= 0), "x should not be < 0"
# AssertionError

# We can catch exceptions with a "try and except block"...

try:
    k = 3 / 0
except Exception as e:
    print(e)
