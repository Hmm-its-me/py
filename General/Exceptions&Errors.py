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
"""Both exceptions and errors are sub-classes of a throwable class.
Exceptions occur during runtime and compile time."""
"""Exceptions can be handled during runtime whereas errors can not
be cannot be handled."""
"""When in runtime an error occurs after passing the syntax test
it is then called an exception or logical type error.
Ex: AttributeError, KeyError, ImportError, IndexError, TypeError"""

try:
    k = 3 / 1
    b = k + 3
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e, "here")
else:
    print("No errors found, Evertyhing is fine.")
finally:
    print("Generally this is used to make some cleaning up...🤔")
# The finally clause runs always no matter if there was an exception or not.
"""Defining our own error class"""
