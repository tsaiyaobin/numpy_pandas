import numpy as np
#-------------------建立多維陣列----------------------

listdata = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
na = np.array(listdata)
print(na) # [ [ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12] ]
print('維度', na.ndim) # 2
print('形狀', na.shape) # (3, 4)
print('數量', na.size) # 12

#-------------------改變陣列形狀:reshape()----------------------
# 例如用 arange 建立一個 1 * 16 的陣列，再利用 reshape 改變為 4*4
adata=np.arange(1,17)
print(adata)
bdata=adata.reshape(4,4)
print(bdata)