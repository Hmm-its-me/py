# Notes

conda create --name "Name..." python=3.x  (if we want a specific version instead of the latest.
in diff envs when we install diff packages using pip or..etc the packages will get installed based on the python version in that environment.

conda activate "Name of env"
conda deactivate

-> To completely remove an env we created...
conda env remove -n "Name of the env we want to remove..."


-> pip install pre-commit
-> Now once check the version using
pre-commit --version

-> create a .pre-commit-config.yaml file
-> Use the command
"pre-commit install"
-> To check whether it is installed at  -> git\hooks\pre-commit


## lists

Lists -> Ordered, mutable, allows duplicate elements
list()
mylist[-1] -> Last element
if "xyz" in mylist: -> To check if anything is in our list (mylist)
.append("xyz") -> To append
.pop() -> To remove the last element.
.remove("xyz") -> Only removes the first occurence of "xyz" in the list
.clear()  -> To erase the whole list.
.reverse() -> To Reverse the order of whole list
.sort()  -> To sort the whole list as per dictionary or integers...if 2 types
            are present inside the list then, it will give error.
            Sorts inplace (means changes our list to sorted list completely)

new_list = sorted(mylist) -> To get sorted version of our list without changing our list.
mylist = curr_list * 5    -> To make our list bigger by x times by repeating our list.

a = mylist[a:b]  -> a = all values in list from index a to b-1;
a = mylist[:]    -> a = all values from start to end;
a = mylist[a:b:c] -> a = all values in list starting from index a to b-1 with steps of 'c'; by default c = 1

## Copying a list (We should not use "=" to create a copy)

list_cpy = mylist.copy()
list_cpy = list(mylist)
list_cpy = mylist[:]

List comprehension [expression and loop our list to make changes...]
l1 = [1,2,3,4,5,6]
l2 = [i*i for i in l1]

# Tuples

Tuples -> Ordered, immutable, allows duplicate elements
Similar to list, but it can not be changed after creation

We can not assign any new value to/in our tuple
mytuple[0] = "not hello" -> It will give assignment not possible error.

len(mytuple) -> gives the length
mytuple.count("xyz") -> Gives no.of non-overlapping "xyz" strings present.
mytuple.index("xyz") -> Gives (0 based) index of first occurence of "xyz"

a = mytuple[a:b]  -> a = all values in list from index a to b-1;
a = mytuple[:]    -> a = all values from start to end;
a = mytuple[a:b:c] -> a = all values in list starting from index a to b-1 with steps of 'c'; by default c = 1

## Unpacking in tuples (number of vars on left side must be = len(mytuple))

mytuple = (1,2,3,4,4,4,4,5,6,7,7,7,7,8)
name, age, city = "Max", 28, "ongole"
i1, *i2, i3 = mytuple
i1 = 1
i3 = 8
And all the elements in between as a list
i2 = [2, 3, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7] -> A list

print(sys.getsizeof(mylist))
print(sys.getsizeof(mytuple))
For the same elements tuple will take less space and is more
Faster to iterate in a tuple than a list

# Dictionary

## Any immutable type can be used as a key in the dictionary

-> Like ints, strings, even tuples... but not lists.

Dictionary -> Key-Value pairs, mutable, ordered.
m1 = {"name": "Suraj", "Age": 19, "City": "Ongole"}

print(m1["name"])
-> Mutable, so we can add a new key-value pair
m1["new pair"] = "value"

.pop("xyz") -> Give key that needs to be deleted.
.popitem()  -> Removes the last item of the dictionary.
del m1["xyz"] -> deleted the key "xyz" present in m1
val = m1["pqr"] -> Returns the value of the key "pqr" and assigns it to val
m1.update(m2)  -> Updates the same keys with values of m2, and also adds
                  keys that are not initially in m1 but in m2

## Copying a dictionary (We should not use "=" to create a copy)

dict_cpy = m1.copy()
dict_cpy = dict(m1)



# Sets

-> Unordered, mutable, No duplicates allowed

.add(x)  -> To add elements into the set
.remove(x) -> To remove this element from the set, Throws a key-value error, if the element is not present in the set.
.discard(x) -> Removes the element if it is there in the set otherwise not...
.clear()  -> Removes all the elements from the set and makes it empty.
.pop()    -> Removes an arbitary element from the set, and also returns it.

## The following operations will not modify our original set.

.union()  -> Union of 2 sets to form a single set
.interesection() -> Takes common elements from both the sets.
.difference()     -> Removes elements of second set which are in 1st one and returns the 1st one after removing them.
.symmetric_difference() -> 1st union of sets and then removes elements present commonly in both the sets from the union.
...............................................................................


.update() -> Updates the 1st one with same as like .union()
.intersection_update() -> Same as .intersection() but here it updates the 1st set with common elements of both the sets.
.difference_update() -> Same as .difference() but updates the 1st set with it.
.symmetric_difference_update() -> 'similarily..'
.issubset() -> Returns true or false based on 1st one is subset of 2nd one or not...
.issuperset() -> similarliy checks and returns boolean
.isdisjoin()  -> Returns true if both sets don't have any common elements.


## Copying a set (We should not use "=" to create a copy), and frozenset

set_cpy = myset.copy()
set_cpy = set(myset)
set_cpy = myset[:]

fs = frozenset([1,2,3,4])
similar to set but it is immutable...like tuples
so we can not use any operations like .add(),.update()....etc...



# Strings

-> Ordered, immutable, For Text Representation

If we want to use single quote or double quote one inside another
then we can use them symmetrically or use a \ character before the inside
quote so that it won't interfere with the outside one.


a = mystring[a:b]  -> a = all values in list from index a to b-1;
a = mystring[:]    -> a = all values from start to end;
a = mystring[a:b:c] -> a = all values in list starting from index a to b-1 with steps of 'c'; by default c = 1
a = mystring[::-1] -> To reverse the string...

s = s + s1 (Concatenation of strings)

.strip()   -> Removes trailing white spaces in the string (" ")
.upper()   -> Changes all the chars to uppercase
.lower()   -> Changes all the chars to lowercase
.startswith("xyz") -> Returns true or false
.endswith("xyz")   -> .......same..........
.find("xyz")       -> Returns the first index where it finds the substring or char "xyz"
.count("xyz")      -> Does not count overlapping substrings...if present in the string
.replace("xyz", "abc") -> Replaces all the instances of "xyz" with "abc";
S.split(" ")  -> Returns a ***List*** of chars or strings...
" ".join(list) -> Joins the chars/strings in the list into one string based on how we are joining

f strings -> f"Hello How are you...{var1} Good Morning {var2}"


# Collections

## Counter

Returns a dictionary with Elements as -> Dictionary keys and their count as dictionary values.

So we can use-> .keys(), .values(), .items() like on dictionary...

.most_common(x) -> Returns a list of x 1st most common tuples of the counter
.elements()     -> Returns an iterator to travle along all the elements of the Counter along with their repetitions

# Numpy

If module import error is comming and
when try to install numpy using
pip3 install numpy   -> it is showing
requirement already satisfied....

Then used this command in the terminal(powershell) and it worked ->

## python -mpip install numpy

The Numpy library provides specialized data structures, functions, and other tools for numerical computing in Python.

Numpy operations and functions are implemented internally in C++, which makes them much faster than using Python statements & loops that are interpreted at runtime.

.dot(a1,a2) -> Gives dot product (integer) of ndarrays a1,a2;
.sum()      -> Gives sum of elements present in the ndarray
.matmul(a1,a2) or a1@a2 -> Gives the resulting matrix which comes by multiplying a1 with a2;


To find the shape of an numpy array go from the outermost brackets
to inside by counting no.of arrays at each stage...

At each stage the no.of elements must be equal otherwise it will give
value Error -> inhomogeneous shape after x stage...

## Note that a2 has to be in proper shape, otherwise we need to use a2.reshape(x,y)

a3 = np.concatenate((a1, a2), axis=0)
