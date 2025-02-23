import pandas as pd
import numpy as np
# Pandas 建立 Dataframe 的語法 : pd.Dataframe(資料 [,index = 索引, column = 欄位])
# index 是橫向列號, column 是欄位名稱, 如果沒有設置就會從 0 開始

arr1 = np.random.randint(50, 101, (4, 5))

df1 = pd.DataFrame(arr1)
print(df1)

#              0   1   2   3   4  <--col
# index--> 0  78  65  74  69  69
#          1  93  89  93  96  58
#          2  86  65  55  87  73
#          3  84  90  96  65  99

arr2 = np.random.randint(50, 101, (4, 5))

df2 = pd.DataFrame(arr2,index = ['王一','李二','張三','黃四']
                   ,columns = ['國','英','數','自','社'])
print(df2)
#      國    英   數   自   社
# 王一  56   87  51  65  83
# 李二  69   64  59  98  55
# 張三  69   59  75  93  58
# 黃四  76  100  93  85  69