import numpy as np
a = np.random.choice(50, size=10, replace=False) # replace=False => 不重複
print('排序前的陣列 : ', a)
print('排序後的陣列 : ', np.sort(a))
print('排序後的索引 : ', np.argsort(a))
# 排序前的陣列 :  [40 25 13 27  5 30  9 32 29 18]
# 排序後的陣列 :  [ 5  9 13 18 25 27 29 30 32 40]
# 排序後的索引 :  [4 6 2 9 1 3 8 5 7 0]

# 用索引到陣列取值
for i in np.argsort(a):
    print(a[i],end=",")
# 5,9,13,18,25,27,29,30,32,40.

b = np.random.randint(0, 10, (3, 5)) # 3 * 5 的二維形狀
print("原陣列內容 : \n", b)
print('將每一行進行排序 : \n', np.sort(b, axis=0)) # axis=0 是行
print('將每一列進行排序 : \n', np.sort(b, axis=1)) # axis=1 是列
# 原陣列內容 : 
# [[2 4 1 0 2]
#  [2 7 7 6 4]
#  [0 7 7 1 3]]
# 將每一行進行排序 : 
# [[0 4 1 0 2]
#  [2 7 7 1 3]
#  [2 7 7 6 4]]
# 將每一列進行排序 : 
# [[0 1 2 2 4]
#  [2 4 6 7 7]
#  [0 1 3 7 7]]