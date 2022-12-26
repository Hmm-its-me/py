# Notes

conda create --name "Name..." python=3.x  (if we want a specific version instead of the latest.
in diff envs when we install diff packages using pip or..etc the packages will get installed based on the python version in that environment.

conda activate "Name of env"
conda deactivate

-> To completely remove an env we created...
conda env remove -n "Name of the env we want to remove..."

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
