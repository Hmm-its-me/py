# hjkl -> Navigation.
# iIaA -> Editing in a line (from command mode to insert mode...)
# xr -> To del, replace characters.

print("Hello world")

mylist = ["cherry", "Apple", "Banana"]
mylist2 = list()

print(mylist2)

print(mylist)
print(mylist[-1])

for i in mylist:
    print(i)

if "Banana" in mylist:
    print("YES")
else:
    print("NO")

mylist.append("Lemon")

print(len(mylist))

mylist.insert(1, "Blue Berry")

for i in mylist:
    print(i)

last = mylist.pop()
print(last)
mylist.append("cherry")
print(mylist)

mylist.remove("cherry")
print(mylist)

mylist.reverse()
print(mylist)

mylist.append("3")
mylist.append("0")

mylist2.append(2)
mylist2.append("here")

mylist.sort()
print(mylist, " ", mylist2)

mylist *= 3
print(mylist)

mylist += mylist2
print(mylist)
print(mylist2)

list_cpy = mylist
list_cpy.append("Appending in the copy")

print(list_cpy)
print(mylist)

# It changes the original list also.

# List comprehension [expression and loop our list to make changes...]
l1 = [1, 2, 3, 4, 5, 6]
l2 = [i * i for i in l1]

print(l1, " ", l2)
