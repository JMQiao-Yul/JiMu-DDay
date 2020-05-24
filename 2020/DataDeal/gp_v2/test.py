import urllib.request
import urllib
import re
import pandas as pd
import pymysql
import os

def getHtml(url):
    """
    抓取网页数据
    """
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    return html

def getStackCode(html):
    """
    抓取网页股票代码
    """
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code

# 东方财富网股票数据连接地址
url = 'http://quote.eastmoney.com/stocklist.html'
# 股票数据文件保存路径
data_path = r'D:\\gp_data\\'
html = getHtml(url)
print(html)
code = getStackCode(html)
code_list = []
for item in code:
    code_list.append(item)

for code in code_list:
    print('正在获取股票%s数据' % code)
    url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+'&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    urllib.request.urlretrieve(url, data_path+code+'.csv')
