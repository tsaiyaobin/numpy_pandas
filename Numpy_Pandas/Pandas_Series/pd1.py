import pandas as pd

#----------Series 是一維的資料陣列--------------
# 資料可用list, tuple, dict, numpy array
se = pd.Series([1, 2, 3, 4, 5])
print(se)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

print(se.values) # [1 2 3 4 5]

print(se.index) # RangeIndex(start=0, stop=5, step=1)

#---------------以相關所引取值----------------
print(se[2]) # 3

print(se[2:5])
# 2    3
# 3    4
# 4    5

