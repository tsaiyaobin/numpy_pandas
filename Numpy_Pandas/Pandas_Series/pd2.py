import pandas as pd

#------------自訂索引及取值--------------
se = pd.Series([1, 2, 3, 4, 5], index = ['a','b','c','d','e'])
print(se)
# a    1
# b    2
# c    3
# d    4
# e    5

print(se['c']) # 3

print(se['a':'c'])
# a    1
# b    2
# c    3


#------------使用字典建立Series--------------
dict1={'Taipei' : '台北', 'Taichung' : '台中', 'Kaoshiung' : '高雄', 'Tainan' : '台南'}
se = pd.Series(dict1)
print(se)
# Taipei       台北
# Taichung     台中
# Kaoshiung    高雄
# Tainan       台南
# dtype: object

print(se.values) # ['台北' '台中' '高雄' '台南']

print(se.index) # Index(['Taipei', 'Taichung', 'Kaoshiung', 'Tainan'], dtype='object')

print(se['Taipei']) # 台北

print(se['Taichung':'Tainan'])
# Taichung     台中
# Kaoshiung    高雄
# Tainan       台南



