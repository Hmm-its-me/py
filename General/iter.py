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
