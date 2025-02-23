import numpy as np

#----------建立同值數列:zeros() & ones()-----------
a = np.zeros(5)
print(a) # [0. 0. 0. 0. 0.]
b = np.zeros((2, 5))
print(b) # [[0. 0. 0. 0. 0.] [0. 0. 0. 0. 0.]]

c = np.ones(5)
print(c) # [1. 1. 1. 1. 1.]
d = np.ones((2, 5))
print(d) # [[1. 1. 1. 1. 1.] [1. 1. 1. 1. 1.]]
