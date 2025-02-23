import numpy as np
#---------建立有序整數陣列:arange()-----------

'''
arange 與 range 相似，語法如下:

numpy.arange( [起始值 ,] 終止值 [, 間隔值] )
'''
# 例如:取 0-30 的偶數做陣列

arr = np.arange(0, 31, 2)
print(arr) # [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30]

#----------建立等距陣列:linspace()-----------
# numpy.linspace(起始值 , 終止值 , 元素個素)
# 例如:由 1 - 15 之間等距的 3 個元素

na = np.linspace(1, 15, 3) 
print(na) # [ 1.  8. 15.]