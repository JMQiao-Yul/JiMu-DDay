import tushare as ts

ts.set_token('27a17eae15d5e9a44e490ccedefc1f10e7b09e98b1747ddb2adeee9f')

pro = ts.pro_api()

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

print(data)