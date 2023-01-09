print("Sai\nSuraj")
# \n -> To insert a new line

print('Hi, Whats\'up?')
# \" -> \ can be used as an escape character, It will not consider the char present nxt to it, except for printing it...

name = "Sai Suraj"

print(name.upper())
print(name.lower().islower())
print(name.capitalize())

print(name, len(name))

# .index() vs .find() -> Both return the index position of first occurence of a substring or char
# If it is not present then .find() will return -1 whereas .index() will throw an error;

num = 3
print(str(num) + " Is my fav number")

print(round(3.2), round(7.7), round(19.5), round(14.499999999))

from math import *

print(
    sqrt(num), floor(3.7), ceil(4.000000000000001)
)  # Here if i keep >= 15 zeros before 1 it is giving 4 only as the answer...

# name = input("Please Enter your name: ")
# age = int(input("How old are you? "))
# print("Heyy! " + name + f" So you are {age} years old 😄")

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]

l1.extend(l2)  # Can be used to easily combine 2 lists together.
print(l1, l2)

l1.append(10)  # Adds a new value to the end of the list.
print(l1)

l1.insert(2, 27)  # Inserts a new value at any position of the list.
print(l1)

l2.extend([1, 2, 3])
l2.sort()
print(l2)
l2.extend([-1, -2, -3])
l3 = sorted(l2)
"""The difference between .sort() and sorted(...) can be seen here."""
print(l3, l2)

# sorted(...) function returns -> a new sequence type containing a sorted version of the given sequence
# Where as .sort() fn returns nothing but makes changes to the original sequence itself.

coordinates = [(2, 3), (-1, -1), (-3, 6), (33, 80)]
print(coordinates[-3])


# functions
def say_hi(name):
    print(f"Heyy, {name}, How are you?")


def say_hello(name):
    return f"Heyy, {name}, You look great."


say_hi("suraj")
print(say_hello("sijafdl"))


def cube(num):
    return pow(num, 3)
    print("came here")


print(cube(3))
res = cube(4)
print(res)

is_tall = True
is_male = False

if (is_tall and is_male):
    print("He is a tall male")
elif (is_tall):
    print("She is a tall woman")
elif (is_male):
    print("He is a short male")
else:
    print("She is a short woman")

# Fn to find the max number among the given 3 numbers


def max_num(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    else:
        return c


print(max_num(1, 2, 3))
max_num(9, 7, 3)  # -> Does not print anything for this
print(max_num(4, 5, 3))


def simp_calc():
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter the operation you want to perform on the numbers?")

    if (op == '+'):
        return a + b
    elif (op == '*'):
        return a * b
    elif (op == '-'):
        return a - b
    elif (op == '/'):
        return a / b
    elif (op == '%'):
        return a % b
    else:
        return "Invalid operator"


print(simp_calc())

months = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "Novemeber",
    "dec": "December"
}

print(months["nov"])
# Using .get(key,default value) we can give a default value for any key...
print(
    months.get(
        "sljfkda",
        "This is the default value we can give, when we don't find the key in the dictionary..."
    ))

for i in range(len(l1)):
    print(l1[i])

for i in l1:
    print(i)

for i in range(len("Sai Suraj")):
    if (i == 0):
        print("First Iteration", )
    else:
        print("Not first")

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

print(ll[0][2], ll[2][1])

for i in range(len(ll)):
    for j in range(len(ll[i])):
        print(ll[i][j], end=" ")

# Or we can also do like this...
print('\n')
for i in ll:
    for j in i:
        print(j, end=" ")
