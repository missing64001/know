



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
import json

M = ['BTS','HTB','CYB','SEER','HT','ETH','OCT','YOYOW','EOS','FIL6','ABT','WAL','THETA']
name_change = {
    'ETH':'ethereum',
    'BTS':'bitshares',
    'OCT':'oraclechain',
    'FIL6':'filecoin',
    'ABT':'arcblock',
    'WAL':'whaletoken',
    'THETA':'thetatoken',

}

def main():
    tinterval = Time_interval(save_data,1/6)
    while True:
        tinterval.run()


def save_data(n=1):
    try:
        data = get_data()
        hmysql.save_data(data,int(time.time()/600)*600)
    except (error.URLError,ValueError,timeout) as e:
        traceback.print_exc()
        time.sleep(600)
        save_data()



def get_data():
    def deal_data(name,price,volume):

        price = str(price)
        if '.' in price:
            price_int,price_wei = price.split('.')
            price_int += price_wei
            price_int = int(price_int)
            price_wei = len(str(price_wei))
        else:
            price_int = int(price)
            price_wei = 0

        volume = str(int(float(volume)))

        return name,price_int,price_wei,volume


    reslst = []


    for m in M:
        try:
            if m == 'CYB':
                reslst.append(deal_data(*get_cyb()))
            name = name_change.get(m,m)
            data = mytoken_set_cookie('https://public.bqi.com/public/v1/ticker?code=%s&convert=CNY' % name)
            data = json.loads(data.decode())[0]
            name,price,volume = m,float(data['price_cny']),int(data['volume_24h_cny'])
            if not price:
                name,price,volume = m,round(float(data['price_usd'])*6.7160,4),int(data['volume_24h_usd'])*6.7160
            print(name,price,volume,end='\r')
            reslst.append(deal_data(name,price,volume))
        except:
            pass
            # traceback.print_exc()

    return reslst

def get_cyb():

    data = mytoken_set_cookie('https://www.mytoken.io/currency/cyb/821689818?legal_currency=CNY')
    text = data.decode()
    from lxml import etree
    html = etree.HTML(text)
    price = html.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[1]/div[2]/div[2]/div[1]/text()')[0]
    volume = html.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[1]/div[3]/div[2]/div[2]/p/text()')[0]
    volume = volume.replace('¥','').replace(',','')
    # volume = round(float(volume)*6.9,2)
    return 'CYB',price,volume

def mytoken_set_cookie(url,t=0):
    t += 1
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    req = request.Request(url, 
                         headers=headers,
                         )

    try:
        response = request.urlopen(req,timeout = 20)
    except timeout as e:
        print('timeout')
        if t < 4:
            return mytoken_set_cookie(url,t)

    return response.read()


if __name__ == '__main__':
    main()