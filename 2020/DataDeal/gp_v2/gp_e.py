# encoding=utf-8
import urllib
import urllib.request

def get_gp_realtime(stack_code):
    url = 'http://hq.sinajs.cn/list=' + stack_code
    html = urllib.request.urlopen(url).read()
    html = html.decode('gb2312')
    print(html)
    data = html.split('=')[1]
    data = data[1:-3]
    data = data.split(',')
    print(data)
    return data


get_gp_realtime('sz002661')
