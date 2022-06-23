import sys
import numpy as np

Y = np.array([0, 0, 1, 1])
A = np.array([1, 1, 0, 0])

Y = np.array([1, 1, 0, 0])
A = np.array([1, 1, 0, 0])

eps = sys.float_info.epsilon
A = np.maximum(eps, np.minimum(1-eps, A))
print("A now: ", A)
m = len(Y)

a = Y * np.log(A)
b = (1-Y) * np.log(1-A)
print("first term: ", a)
print("second term: ", b)
print("sum of first and second", a + b)

cost = -1/m * np.sum(Y * np.log(A) + (1-Y) * np.log(1-A))
print(cost)