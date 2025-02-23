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
a = np.random.randint(100, size = 50)
print('陣列內容 : \n', a)
# 陣列內容 : 
# [94 69 16 26 82 98 14 95 81 96 93 57 81 14 94 55 84 46  9 19  5 98 62 81
# 58 85 66 19 23 15 28 77 30 62 14 78 45  9 37 51  3 47 11 49 60 42 44 38
# 66 18]

print('1.標準差 : ', np.std(a))
print('2.變異數 : ', np.var(a))
print('3.中位數 : ', np.median(a))
print('4.百分比值 : ', np.percentile(a,80))
print('5.最大最小差值 : ', np.ptp(a))

# 1.標準差 :  27.957288852819758
# 2.變異數 :  781.6099999999999
# 3.中位數 :  56.5
# 4.百分比值 :  72.2
# 5.最大最小差值 :  88