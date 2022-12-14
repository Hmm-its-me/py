s = "Hello world"
s1 = "I'm a programmer"
s2 = 'I\'m a programmer'
# \ is used an escape character. The char next to it will only get printed but not considered
print(s, " ", s1, " ", s2)

s0 = """This 3 quotes is used for multi line strings
-> 2nd line \
-> 3rd line...but used back slash so newline character is escaped."""

print(s0)

s = s[::-1]
# Reversing the string using indexing...
print(s)

s = s[::-1]
s1 = s + " " + s1

print(s1)

for i in s:
    print(i)

if 'quo' in s0:  # We can directly check for substrings also...
    print("YES")
else:
    print("NO")

s3 = "           hello...           "
# Removes trailing and ending white spaces...
# It do not change my original string, as strings are immutable
print(s3.strip())
print(s3.upper())
print(s3.lower())
print(s3.startswith("world"))
# From the start it must be there...
print(s3.startswith("           hello"))
print(s1.endswith("programmer"))

print(s1.find('pro'))  # Returns the index at which this substring starts...
# Returns -1 if not present in the string...

print(s1)
print(s1.count('m'))
print(s1.count('A'))

print(s1.replace('world', 'Universe'))
print(s1)
# Replaces all instances of 'm' with 'x';
print(s1.replace('m', 'x'))

mys = "Hello How are You?"
m1 = mys.split(
)  # Returns a list of strings (breaks when there is " " by default)
print(m1)

m2 = ' '.join(m1)
print(m2)

s = f"Hello how are you {3*3*3}, I am happy and I am {s2}"

print(s)
