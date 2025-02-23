import numpy as np

''' 
sum : 加總        | median : 中位數
prod : 乘積       | argmin : 最小元素索引值
mean : 平均值     | argmax : 最大元素索引值
min : 最小值      | cumsum : 陣列元素累加
max : 最大值      | cumprod : 陣列元素累積
std : 標準差      | percentile : 以百分比顯示陣列中指定值
var : 變異數      | ptp : 最大值與最小值差

'''
a = np.arange(1,10).reshape(3,3)
print('陣列內容:',a)
# 陣列內容:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print('1.最小值與最大值:\n', np.min(a), np.max(a))
# 1.最小值與最大值:
# 1 9

print('2.每一行最小值與最大值:\n', np.min(a, axis=0), np.max(a, axis=0))
# 2.每一行最小值與最大值:
# [1 2 3] [7 8 9]

print('3.每一列最小值與最大值:\n', np.min(a, axis=1), np.max(a, axis=1))
# 3.每一列最小值與最大值:
# [1 4 7] [3 6 9]

print('4.加總、乘積及平均:\n', np.sum(a), np.prod(a), np.mean(a))
# 4.加總、乘積及平均:
# 45 362880 5.0

print('5.每一行加總、乘積及平均:\n', np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
# 5.每一行加總、乘積及平均:
# [12 15 18] [ 28  80 162] [4. 5. 6.]

print('6.每一列加總、乘積及平均:\n', np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))
# 6.每一列加總、乘積及平均:
# [ 6 15 24] [  6 120 504] [2. 5. 8.]

