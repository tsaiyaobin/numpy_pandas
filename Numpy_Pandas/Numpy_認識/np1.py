import numpy as np

#-------------建立陣列:array()-------------

np1 = np.array([1, 2, 3, 4]) # [1 2 3 4] 
np2 = np.array((1, 2, 3, 4)) # [1 2 3 4]

print(np1,np2)
print(type(np1),type(np2)) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>

#---------設定陣列資料格式:dtype------------

na = np.array([1, 2, 3, 4] , dtype = int) 
print(na) # [1 2 3 4] 
na = np.array([1, 2, 3, 4] , dtype = float) 
print(na) # [1. 2. 3. 4.]





























