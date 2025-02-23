import pandas as pd

'''
read_csv	匯入表格式文字資料（*.csv）
read_excel	匯入 Microsoft Excel 資料（*.xlsx）
read_sql	匯入 SQLite 資料庫資料（*.sqlite）
read_json	匯入 Json 格式文字資料（*.json）
read_html	匯入網頁中表格資料（*.html）
'''
#------------使用 Pandas 讀取資料-------------
# 語法:pandas.read_csv(檔案名稱 [, header = 布林值, index_col = 布林值,
#                             encoding = 編碼, sep = 分隔符號])

data = pd.read_csv("scores2.csv", header = 0, index_col = 0, encoding = 'big5')
print(data)
print(type(data))
#      國    英    數    自     社
# 王一    65  92    81   92  64
# 李二    90  82    82   28  86
# 張三    81  75    73   52  94
# 黃四    79  56    52   15  86
# <class 'pandas.core.frame.DataFrame'>


'''
to_csv	將資料儲存為表格式文字資料（*.csv）
to_excel	將資料儲存為 Microsoft Excel 資料（*.xlsx）
to_sql	將資料儲存為 SQLite 資料庫資料（*.sqlite）
to_json	將資料儲存為 Json 格式文字資料（*.json）
to_html	將資料儲存為網頁中表格資料（*.html）
'''
#------------使用 Pandas 儲存資料-------------
# 語法:pandas.to_csv(檔案名稱 [, header = 布林值, index = 布林值,
#                             encoding = 編碼, sep = 分隔符號])
# 參數 header index 的設定值為 True ，代表是否保留欄位列或索引欄

scores = {'國' : {'王一':65, '李二':90, '張三':81, '黃四':79},
          '英' : {'王一':92, '李二':82, '張三':75, '黃四':56},
          '數' : {'王一':81, '李二':82, '張三':73, '黃四':52},
          '自' : {'王一':92, '李二':28, '張三':52, '黃四':15},
          '社' : {'王一':64, '李二':86, '張三':94, '黃四':86}}
df = pd.DataFrame(scores)
print(df)
df.to_csv("scores3", encoding = "utf-8-sig")

