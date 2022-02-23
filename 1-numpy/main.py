#!/usr/bin/env python
import numpy as np

#1a. Create a null vector of size 10 but the fifth value which is 1
vec1a = np.zeros(10)
vec1a[9] = 1
print('1a)', vec1a, '\n')

#1b. Create a vector with values ranging from 10 to 49 
vec1b = np.linspace(10, 49, 10)
print('1b)', vec1b, '\n')

#1c. Reverse a vector (first element becomes last)
vec1c = np.flip(vec1b)
print('1c)', vec1c, '\n')

#1d. Create a 3x3 matrix with values ranging from 0 to 8
vec1d = np.linspace(0, 8, 9) 
mat1d = vec1d.reshape([3, 3])
print('1d)', mat1d, '\n')

#1e. Find indices of non-zero elements from [1,2,0,0,4,0]
vec1e = np.array([1,2,0,0,4,0])
print('1e)', np.where(vec1e > 0), '\n')

#1f. Create a random vector of size 30 and find the mean value
vec1f = np.random.rand(30)
print('1f)', np.mean(vec1f), '\n')

#1g. Create a 2d array with 1 on the border and 0 inside
vec1g = np.linspace(1, 1,9)
vec1g[4] = 0 
vec1g = vec1g.reshape([3, 3])
print('1g)', vec1g, '\n')

#1h. Create a 8x8 matrix and fill it with a checkerboard pattern
vec1h = np.zeros(8*8)
vec1h = vec1h.reshape([8, 8])
vec1h[0:8:2, 0:8:2] = 1
vec1h[1:9:2, 1:9:2] = 1
print('1h)\n', vec1h, '\n')

#1i. Create a checkerboard 8x8 matrix using the tile function
vec1i = np.array([[1, 0],[0, 1]])
vec1i = np.tile(vec1i, [4, 4])
print('1i)\n', vec1i, '\n')

#1j. Given a 1D array, negate all elements which are between 3 and 8, in place
vec1j = np.arange(11)
print(a, b)
vec1j = np.where(np.logical_and(a, b), vec1j*-1, vec1j)
print('1j)\n', vec1j, '\n')

#1k. Create a random vector of size 10 and sort it
vec1k = np.random.rand(10)
print('1k)', np.sort(vec1k), '\n')

#1l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.where(A == B)
print('1l)', equal, '\n')

#1m. How to convert an integer (32 bits) array into a float (32 bits) in place?
print('1m)')
vec1m = np.arange(10, dtype=np.int32)
print(vec1m.dtype)
vec1m = np.int64(vec1m)
print(vec1m.dtype, '\n')

#1n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = C.diagonal()
print('1n)', D, '\n')

