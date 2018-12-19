from .h05_hmysql import Mysql
import sys
import os
import time,datetime
from pprint import pprint




def save_data(data,t):
    for da in data:
        name,value_int,value_wei,volume = da
        MYSQL.exec('insert into assets_value values(null,"%s",%s,%s,%s,%s);'%
            (name,value_int,value_wei,volume,t))

def change_fund(asset_name,volume,exchange_name,create_time=None):
    if not create_time:
        create_time = int(time.time())
    MYSQL.exec('insert into my_assets values(null,"%s",%s,"%s",%s);'%
            (asset_name,volume,exchange_name,create_time))



def get_all_amount_all_exchange():
    sql_s = '''
                SELECT exchange,name,sum(volume) from my_assets group by exchange,name;
            '''
    data = MYSQL.get_exec(sql_s)
    [     print('%10s %10s %10s'%    (da[0],da[1],int(da[2]))  ) for da in data ]

    sql_s = '''
                SELECT name,exchange,sum(volume) from my_assets group by name asc,exchange;
            '''
    data = MYSQL.get_exec(sql_s)
    [     print('%10s %10s %10s'%    (da[0],da[1],int(da[2]))  ) for da in data ]


def get_all_amount_by_exchange():

    data = MYSQL.get_exec(
        '''
            SELECT exchange,sum(fund) as fund from
            
            (SELECT t1.volume*t2.value_int/power(10,value_wei) as fund,exchange
            FROM my_assets as t1
            LEFT JOIN (
                        SELECT t1.id,t1.name,value_int,value_wei from (select name,max(id) as id from assets_value group by name) as t1
                        LEFT JOIN assets_value as t2 on t1.id = t2.id
            ) as t2 
            ON t1.name=t2.name) as tt
            group by exchange
            ;
        '''
        )
    # pprint(data)
    res = 0
    for da in data:
        if da[1]:
            res += da[1]



    lst = []
    for da in data:
        if da[1]:
            lst.append([da[0],da[1],da[1]/res *100])
    lst.sort(key=lambda x:x[2])

    res = []
    for l in lst:
        res.append('%10s %10d %7.3f%%' % (l[0],l[1]/10,l[2]))
    return res





def get_all_amount_by_coin():

    data = MYSQL.get_exec(
        '''
            SELECT t1.name,t1.volume*t2.value_int/power(10,value_wei) as fund,t1.volume
            FROM (select name,sum(volume) as volume from my_assets group by name) as t1
            LEFT JOIN (
                        SELECT t1.id,t1.name,value_int,value_wei from (select name,max(id) as id from assets_value group by name) as t1
                        LEFT JOIN assets_value as t2 on t1.id = t2.id
            ) as t2 
            ON t1.name=t2.name;
        '''
        )
     # LEFT JOIN (select a.* from assets_value as a where id = (select max(id) from assets_value where a.name=name)) as t2 
    # pprint(data)
    # 
    # 
    # 
    # 


    res = 0
    for da in data:
        if da[1]:
            res += da[1]
    date = MYSQL.get_exec('SELECT create_time from assets_value group by id desc limit 1;')


    timeStamp = int(date[0][0])


    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(otherStyleTime)
    thelastreslst = []
    # print(res)
    thelastreslst.append(otherStyleTime)
    thelastreslst.append('%.3f' %(res/10))



    lst = []
    for da in data:
        if da[1]:
            lst.append([da[0],da[1]/10,da[1]/res *100,int(da[2]),da[1]/int(da[2])])
    lst.sort(key=lambda x:x[2])
    # pprint(lst)   
    for l in lst:
        x = ('%10s %10d %7.3f%% %10s %10.4f'% (*l,) )
        thelastreslst.append(x)


    x = []
    labels = []
    for l in lst:
        x.append(l[2])
        labels.append(l[0])

    if timeStamp + 20 * 60 < time.time():
        ss = '---------------------------------------------------time over---------------------------------------------------'
        thelastreslst.insert(0,ss)
    else:
        thelastreslst.insert(0,'ok')

    return thelastreslst

def getres():
    global MYSQL
    MYSQL = Mysql('120.79.41.9','my_blockchain_assets','my_blockchain_assets',db='my_blockchain_assets')
    


    res1 = get_all_amount_by_exchange()

    res2 = get_all_amount_by_coin()

    res = res2[:3] + ['\n'] + res1 + ['\n'] + res2[3:]
    return res

