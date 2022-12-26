import numpy as np
# Aliasing numpy as np

a1 = np.array([1, 2, 3])
print(a1)
print(type(a1))  # similar to lists in python in some parts...

a2 = np.array([1, 4, 9])

a3 = np.dot(a1, a2)
print(a3)

# We can do like this also...
a4 = a1*a2
print(a4, " ", a4.sum())
