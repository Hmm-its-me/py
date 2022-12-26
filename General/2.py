import sys
mytuple = ("hello", "world", 123)
print(type(mytuple))
print(mytuple)

mytuple2 = ("just one entry")
print(type(mytuple2))
print(mytuple2)

mytuple2 = ("one entry with comma", )
print(type(mytuple))


mytuple3 = tuple([1, 2, 3, "from a list"])
print(mytuple3)

for item in mytuple:
    print(item)


if 1 in mytuple3:
    print("yes")
else:
    print("NO")


# We can not assign any new value to/in our tuple
# mytuple[0] = "not hello" -> It will give assignment not possible error.

mytuple = (1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8)
mylist = [1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8]
mytuple2 = ("Suraj🙂", 19, "hello")
print(mytuple.count(6))
print(mytuple.index(4))

name, age, city = mytuple2
print(name)
print(age)
print(city)

i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)


print(sys.getsizeof(mylist))
print(sys.getsizeof(mytuple))
# For the same elements tuple will take less space and is more
# Faster to iterate in a tuple than a list
