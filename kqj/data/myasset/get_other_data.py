import urllib
import urllib.parse
import urllib.request
import requests

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


def get_wal_orderBook(id_ = 29):
    url = 'https://www.whaleex.com/BUSINESS/api/public/orderBook/symbol/%s' % id_
    params = {'level':'20'}
    data = http_get_request(url, params)
    asks = data['asks']
    bids = data['bids']

    asks = [ ['%9.2f%%' %(float(ask['price'])*100),ask['quantity']] for ask in asks[::-1]]
    bids = [ ['%9.2f%%' %(float(bid['price'])*100),bid['quantity']] for bid in bids]
    asks = [  '%s %12.2f' %(ask[0],float(ask[1]))         for ask in asks]
    bids = [  '%s %12.2f' %(bid[0],float(bid[1]))         for bid in bids]


    asks = '\n'.join(asks)
    bids = '\n'.join(bids)


    res = asks + '\n\n' + bids
    return res

    