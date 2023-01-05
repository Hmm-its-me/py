# Collections: Counter, namedtuple, OrderedDict, Defaultdict, deque
from collections import *

# Counter
s = "aaaaabbbcccc"
myc = Counter(s)

print(myc)
print(myc.keys(), " ", myc.items(), " ", myc.values())

print(myc.most_common(1), " ",
      myc.most_common(2)[1], " ",
      myc.most_common(2)[1][0])
print(list(myc.elements()), ", ", tuple(myc.elements()))

# namedtuple

point = namedtuple("point", 'x,y')
pt1 = point(1, 3)
pt2 = point(-3, -3)
print(pt1, pt1.x, pt1.y, sep=", ")

print(abs(pt1.x - pt2.x), abs(pt2.y - pt1.y))

# OrderedDict
# -> Just like a normal dictionary but it will remember the order in which we inserted the keys
# But since python3.7 it is not needed as dictionary itself is acting in the same way

od = OrderedDict()
od['3'] = "three"
od['2'] = "two"
od['1'] = "one"

print(od)

# Defaultdict
# -> Just like a normal dictionary but it will have a default value for any keys

d = defaultdict(int)
#d = defaultdict(str)
d['b'] = 1
d['a'] = 2
d['c'] = 3

print(d, d['d'], d['f'])

dq = deque()

dq.append(1)
dq.append(2)

dq.appendleft(3)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.clear()
print(dq)

dq.extend(["ba", 'b', 'c'])
print(dq)

dq.rotate(1)
# Rotates the order of elements by 1
print(dq)

dq.rotate(-1)
print(dq)
