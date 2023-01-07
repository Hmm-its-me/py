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


class ValueHighError(Exception):
    pass


class ValueSmallErro(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_num(x):
    if (x > 100):
        raise ValueHighError('Value is too high, Please decrease it')
    elif (x < 5):
        raise ValueSmallErro('Value is too small, Please increase it', x)


try:
    test_num(3)
except Exception as e:
    print(e)
    print(e.message)
    print(e.value)

try:
    test_num(300)
except Exception as e:
    print(e)
