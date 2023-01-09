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

name = input("Please Enter your name: ")
age = int(input("How old are you? "))

print("Heyy! " + name + f" So you are {age} years old 😄")
