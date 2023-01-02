myset = {1, 1, 1, 2, 2, 2, 3, 3, 4}
print(myset)

myset2 = set([2, 3, 4, 5, 2, 1, 3, 4, 4])
print(myset2)

myset3 = set("Hello world")
print(myset3)
# Notice the arbitary order in the output...

s = set()
print(type(s), " ", s)

s.add(1)
s.add(2)
s.add(3)
print(s)

s.remove(2)
print(s)

s.discard(2)
print(s)

s.clear()
s.add("abc")
s.add("efg")
s.add("hij")

print(s)
print(s.pop())
# Removed "abc" this time...might remove another one when it is runned again a few times.

for i in s:
    print("iterating:", i)

if 1 in myset:
    print("Yayy!")

odds = {1, 3, 5, 7}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

v = evens.intersection(odds)
# Empty...
print(v)

k = evens.intersection(primes)
print(k)

j = odds.union(primes)
print(j)

diff1 = primes.difference(evens)
print(diff1)

diff2 = evens.symmetric_difference(primes)
print(diff2)

odds.update(primes)
print(odds)

a = frozenset([1, 2, 3, 4])
#a.add(3)
print(a)
