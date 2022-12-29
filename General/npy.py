import numpy as np

# Aliasing numpy as np

a1 = np.array([[1, 2, 3]])
print(a1)
print(type(a1))  # similar to lists in python in some parts...

a2 = np.array([1, 4, 9])

a3 = np.dot(a1, a2)
print(a3)

# We can do like this also...
a4 = a1 * a2
print(a4, " ", a4.sum())

# Multi dimensional arrays...
b1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(b1, " ", b1.shape, " ", b1.size)

# To find the shape of an numpy array go from the outermost brackets
# to inside by counting no.of arrays at each stage...
print("\n")
c1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 1, 1], [2, 2, 2]],
               [[5, 6, 7], [8, 9, 10]]])
print(c1, " ", c1.shape, " ", c1.size)

# At each stage the no.of elements must be equal otherwise it will give
# value Error -> inhomogeneous shape after x stage...

m1 = a1 @ a2
m2 = np.matmul(a1, a2)
print(m2, " ", type(m2))
print(m1)

print(a1.shape, " ", a2.shape)
a3 = np.concatenate((a1, a2.reshape(1, 3)), axis=1)
a4 = np.concatenate((a1, a2.reshape(1, 3)), axis=0)
print(a3, "\n \n", a4)
