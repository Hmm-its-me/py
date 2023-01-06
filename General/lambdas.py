# lambda arguments: expression

add = lambda x, y: x + y
print(add(3, 4))
print(add(99, 1))

hypo = lambda x, y: pow(x**2 + y**2, 0.5)

print(hypo(3, 4))
print(hypo(5, 12))

# lambda fns are one line functions used generally when we want to create a short fn that is used only once
# Or they are used as an arguments to higher order functions

points = [(1, 2), (15, 1), (5, -1), (10, 4)]

ps = sorted(points)
print(points)
print(ps)

# lambda fn tells that comparisions should be done based on y values of points...
ps = sorted(points, key=lambda x: x[1])
print(ps)


# Insted of this fn only, we can use the lambda fn directly.
def sort_by_y(x):
    return x[1]


ps1 = sorted(points, key=sort_by_y)
print(ps1)

# If we want to sort the points according to sum value of them.

ps2 = sorted(points, key=lambda x: x[0] + x[1])
print(ps2)

# map(func, sequence/container)

a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)

print(b, list(b))
# But this can also be done using list comprehension more easily.

c = [x * 2 for x in a]
print(c)

# Filter(func, sequence/container)
# Here the func should return True/False and filter fn will return all the elements for which fn evaluates as true;

b = filter(lambda x: x % 2 == 0, a)
print(b, list(b))

# Here also we can use the list comprehension directly
c = [x for x in a if (x % 2 == 0)]
print(c)

# reduce(func, sequence/container)
# It repeatedly apply's the fn to the elements of the container and returns a single value/element
from functools import reduce

# The func used for reduce should have 2 argumnets atleast 🤔
b = reduce(lambda x, y: x / y, a)
print(b)
