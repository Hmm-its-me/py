m1 = {"name": "Suraj", "Age": 19, "City": "Ongole"}

print(m1["name"])
m1["new pair"] = "value"
print(m1)

m1["Age"] = 93
print(m1)

del m1["new pair"]
print(m1)

m1.pop("Age")
print(m1)

m1["key"] = 27
print(m1)
m1.popitem()
print(m1)

if "name" in m1:
    print(m1["name"])

try:
    print(m1["lastname"])
except:
    print("Key not found...")


for i in m1:
    print(i, " ", m1[i])

# OR

for i, j in m1.items():
    print(i, ":", j)

for i in m1.keys():
    print(i)

for i in m1.values():
    print(i)


m1 = {"Name": "Suraj", "City": "Ongole", "Age": 19, "lol": "😂"}
m2 = {"Name": "Hacker", "City": "Hacks", "Age": 27, "New": 729}

m1.update(m2)
print(m1)
print(m2)

t1 = (3, 6)
m3 = {t1: 9, 1: 1, (33, 27): 60}
print(m3)
