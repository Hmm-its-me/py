# Notes...

1. lists
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
a = mylist[a:b:c] -> a = all values in list starting from index a to b-1 with steps of 'c';

## To copy a list (We should not use "=" to create a copy).

list_cpy = mylist.copy()
list_cpy = list(mylist)
list_cpy = mylist[:]

List comprehension [expression and loop our list to make changes...]
l1 = [1,2,3,4,5,6]
l2 = [i*i for i in l1]








