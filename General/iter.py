from itertools import *
# product, permutations, combinations, accumulate, groupby, and
# infinite iterators...

a = [1, 2]
b = [2, 3]

p = product(a, b)
print(list(p))

print(list(product(a, b, repeat=2)))

q = permutations(a)
print(list(q))

print(list(permutations([1, 2, 3])))
c = [1, 2, 3]

print(list(permutations(c, 2)))
# The second argument tells the size of each permutation that should be taken

comb = combinations(range(1, 4), 2)  # Here 2nd argument is mandatory
print(list(comb))
# prints all successive combinations possible..
# Observe different from permuations

comb_repl = combinations_with_replacement(range(1, 4), 2)
print(list(comb_repl))

a = [1, 2, 3, 4, 5]
print(list(accumulate(a)))

import operator

print(list(accumulate(a, func=operator.mul)))
print(list(accumulate(a, func=max)))
print(list(accumulate(a, func=min)))

# New..🤔
k = groupby(a, lambda x: x < 3)  # Grouping all elements with value <3

for key, value in k:
    print(key, ":", list(value))

p = [{
    "Age": 3,
    "Name": "Suraj"
}, {
    "Age": 3,
    "Name": "sfhdkas"
}, {
    "Age": 6,
    "Name": "askjfdl"
}]

k1 = groupby(p, lambda x: x["Age"])

for key, value in k1:
    print(key, list(value))

# count, cycle, repeat

for i in count(
        33
):  # starts from a number and goes upto infinity if not stopper anywhere
    if (i == 99):
        break
    print(i)

# Iterates cyclically infinite times through the container until stopped
cn = 0
for i in cycle(a):
    if (cn == 3):
        break
    print(i)
    if (i == 5):
        cn += 1

for i in repeat(
        a, 4):  # prints the container or data infinite times or unitl stopped
    print(i)  # 2nd argument tells no.of times we need to repeat it.
