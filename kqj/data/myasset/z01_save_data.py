


print('v 1.01')
import sys
import os
paths = [r'C:\python\my',r'F:\my',r'/home/uftp/my']
for path in paths:
    if os.path.exists(path):
        sys.path.insert(1,path)
        from F00_myfn.h07_time_interval import Time_interval
        break
else:
    raise ValueError('time_interval is not import')

from http import cookiejar
from urllib import parse
from urllib import request
from urllib import error
import re
from pprint import pprint
import time
from lxml import etree
from socket import timeout
import hmysql
from hmysql import MYSQL
import traceback

def main():
    tinterval = Time_interval(save_data,1/6)
    while True:
        tinterval.run()


def save_data(n=1):
    try:
        data = get_mytoken_data()
        hmysql.save_data(data,int(time.time()/600)*600)
    except (error.URLError,ValueError,timeout) as e:
        traceback.print_exc()
        time.sleep(600)
        save_data()

def get_mytoken_data():
    data = mytoken_set_cookie('https://m.feixiaohao.com/userticker/')


    res = get_mytoken_data_by_xpath(data.decode(errors='ignore'))
    return res

def mytoken_set_cookie(url):
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'usid=3c42b7ca8ecc0e8d; UM_distinctid=1656973f5f03c-06e933ef724dcb-37664109-13c680-1656973f60047b; _ga=GA1.2.1707289407.1537342699; _gid=GA1.2.2051815049.1545120418; browsemode=mobile; CNZZDATA1263003344=1426467563-1545118054-https%253A%252F%252Fwww.feixiaohao.com%252F%7C1545118054; headerad=0.3204790337088883#24; Hm_lvt_192e611c7ffa4b2f8a5047e5cf45403f=1545120410,1545120556; distinctuid=31dbe2dc-57c0-4a44-91eb-b2a3f45b5695; fxhuid=wHf4DKJtGxL5hg9z2LRAKw==; loginid=kenZD2SOvAesaHOsTUGZEA==; Hm_lpvt_192e611c7ffa4b2f8a5047e5cf45403f=1545121158',
    'Host':'m.feixiaohao.com',
    'Referer':'https://m.feixiaohao.com/',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    req = request.Request(url, 
                         headers=headers,
                         )

    try:
        response = request.urlopen(req,timeout = 20)
    except timeout as e:
        print('timeout')
        return mytoken_set_cookie(url)
    

    return response.read()
    

    # with open("myRenren.html", "wb") as f:
    #     f.write(response.read())


def get_mytoken_data_by_xpath(data):
    filename = 'get_mytoken_data_by_xpath.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(data)


    root = etree.HTML(data)
    isright = root.xpath('/html/body/div[3]/div[2]/div[1]/h1/text()')
    if isright != ['自选']:
        raise ValueError('get wrong source')
    items = root.xpath('//*[starts-with(@id,"tr")]')

    reslst = []
    for item in items:
        num = item.xpath('td')
        
        if len(num) != 8:
            continue
        name = item.xpath('td[2]/a/text()')[1].strip()[:-4]
        price = item.xpath('td[3]/span/text()')[0].strip('\xa5')
        volume = item.xpath('td[7]/span/text()')[0].strip('\xa5')






        price = price.replace(',','')
        if '.' in price:
            price_int,price_wei = price.split('.')
            price_int += price_wei
            price_int = int(price_int)
            price_wei = len(str(price_wei))
        else:
            price_int = int(price)
            price_wei = 0
        volume = volume.replace(',','')
        if '万' in volume:
            volume = float(volume.replace('万','')) * 10000
        elif '亿' in volume:
            volume = float(volume.replace('亿','')) * 100000000
        volume = str(int(float(volume)))
        reslst.append((name,price_int,price_wei,volume))
    return reslst

if __name__ == '__main__':
    main()