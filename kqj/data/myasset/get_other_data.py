import urllib
import urllib.parse
import urllib.request
import requests
import time

def main():
    from pprint import pprint
    data = get_wal_data()
    print(data)


def http_get_request(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    if add_to_headers:
        headers.update(add_to_headers)
    postdata = urllib.parse.urlencode(params)
    response = requests.get(url, postdata, headers=headers, timeout=10) 
    try:
        
        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("httpGet failed, detail is:%s,%s" %(response.text,e))
        return


def bingdata(da1,da2):

    da1 = da1.split('\n')
    da2 = da2.split('\n')

    if len(da1)>len(da2):
        da2 += [' '* len(da2[0])]*(len(da1)-len(da2))
    elif len(da1)<len(da2):
        da1 += [' '* len(da1[0])]*(len(da2)-len(da1))

    data = [ (d1 if d1 else ' '*23)           +'  '+d2 for d1,d2 in zip(da1,da2)]



    data = '\n'.join(data)

    return data

def get_wal_data(id_ = 29):
    def setdate(i):
        x = time.strftime('%d %H:%M:%S',time.localtime(i/1000))
        return x



    url = 'https://www.whaleex.com/BUSINESS/api/public/lastTrade?symbolId=%s&size=30' % id_
    params = {}
    data = http_get_request(url, params)




    data = [ ['--' if da['bidAsk'] == 'B' else '  ',da['price'],da['quantity'],int(da['timestamp'])] for da in data ]

    data = [ '%s %4.2f%% %10.2f %s' % ( da[0],float(da[1])*100,float(da[2])    ,  setdate(da[3]) ) for da in data ]

    resdata = '\n'.join(data)




    url = 'https://www.whaleex.com/BUSINESS/api/public/orderBook/symbol/%s?level=20' % id_
    params = {}
    data = http_get_request(url, params)
    # print(data)
    asks = data['asks']
    bids = data['bids']

    asks = [ ['%9.2f%%' %(float(ask['price'])*100),ask['quantity']] for ask in asks[::-1]]
    bids = [ ['%9.2f%%' %(float(bid['price'])*100),bid['quantity']] for bid in bids]
    asks = [  '%s %12.2f' %(ask[0],float(ask[1]))         for ask in asks]
    bids = [  '%s %12.2f' %(bid[0],float(bid[1]))         for bid in bids]


    asks = '\n'.join(asks)
    bids = '\n'.join(bids)


    res = asks + '\n\n' + bids



    
    return bingdata(res,resdata)

if __name__ == '__main__':
    main()