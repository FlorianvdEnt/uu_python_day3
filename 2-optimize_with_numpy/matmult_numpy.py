# Program to multiply two matrices using nested loops
import random
import numpy as np
import time

N = 250

X = np.random.randint(0, 100, [N, N])
Y = np.random.randint(0, 100, [N, N+1])
result = np.matmul(X, Y)

for r in result:
    print(r)
