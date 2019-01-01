import sys
import os
import time,datetime
from pprint import pprint

paths = [r'C:\python\my',r'F:\my',r'/home/uftp/my']
for path in paths:
    if os.path.exists(path):
        sys.path.insert(1,path)
        from F00_myfn.h05_hmysql import Mysql
        break
else:
    raise ValueError('Mysql is not import')


# MYSQL.exec(create_database)
# MYSQL.exec(articles_sql_s)
# MYSQL.exec(context_md5_sql_s)

# my_blockchain_assets

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


def show_pie(labels,x):
    # from __future__ import unicode_literals
    import matplotlib.pyplot as mp
    mp.figure('Pie', facecolor='lightgray')
    mp.title('Pie', fontsize=20)
    mp.pie(x=x,labels=labels, autopct='%d%%', shadow=True, startangle=90)
    mp.axis('equal')
    mp.show()
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




    print(res)



    lst = []
    for da in data:
        if da[1]:
            lst.append([da[0],da[1],da[1]/res *100])
    lst.sort(key=lambda x:x[2])
    pprint(lst)
    

    x = []
    labels = []
    for l in lst:
        x.append(l[2])
        labels.append(l[0])
    show_pie(labels,x)





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


    timeStamp = int(date[0][1])


    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    print(otherStyleTime)

    print(res)



    lst = []
    for da in data:
        if da[1]:
            lst.append([da[0],da[1],da[1]/res *100,int(da[2]),da[1]/int(da[2])])
    lst.sort(key=lambda x:x[2])
    # pprint(lst)   
    for l in lst:
        print('%10s  %15d  %10.3f%%  %10s %10.4f'% (*l,) )



    x = []
    labels = []
    for l in lst:
        x.append(l[2])
        labels.append(l[0])

    if timeStamp + 20 * 60 < time.time():
        ss = '---------------------------------------------------time over---------------------------------------------------'
        print('-'*len(ss))
        print('-'*len(ss))
        print(ss)
        print('-'*len(ss))
        print('-'*len(ss))
    show_pie(labels,x)




    '''
        
        方法一：
        select * from (select * from assets_value order by id desc) as a group by a.name

        方法二：
        select a.* from assets_value as a where id = (select max(id) from assets_value where a.name=name)

        方法三：
        select a.* from assets_value as a where not exists (select * from assets_value where name=a.name and id>a.id)

        方法四：
        select a.* from assets_value as a where exists (select count(*) from assets_value where name=a.name and id>a.id having count(*)=0)


        SELECT t1.name,t1.volume*t2.value_int/power(10,value_wei) as fund,t1.volume,t2.value_int
        FROM (select name,sum(volume) as volume from my_assets group by name) as t1
        LEFT JOIN (select a.* from assets_value as a where id = (select max(id) from assets_value where a.name=name)) as t2 
        ON t1.name=t2.name;

    '''
    '''
        select name from assets_value where id inner join my_assets on assets_value.name = my_assets.name
    

        select * from (select * from assets_value order by id desc) as a group by a.name;

        insert into assets_value values(null,"CNY",1,0,1,1535119200);

    '''

def main():
    global MYSQL
    MYSQL = Mysql('120.79.41.9','my_blockchain_assets','my_blockchain_assets',db='my_blockchain_assets')
    # change_fund('EOS',10590.4645,'bigone')
    # change_fund('USDT',31197.97,'bigone')
    # change_fund('ETH',56.108,'bigone')
    # change_fund('OCT',49301.50,'bigone')

    # change_fund('USDT',43432.73,'huobi')
    # change_fund('EOS',2723.99,'huobi')
    # change_fund('HT',12734.76,'huobi')


    # change_fund('ETH',1.48,'imtoken')
    # change_fund('YOYOW',451463,'imtoken')
    # change_fund('RISK',3330000,'imtoken')


    # change_fund('ETH',5,'bts')
    # change_fund('BTS',3807+904117+1093,'bts')
    # change_fund('CNY',5185-240000+1762,'bts')
    # change_fund('EOS',5819.77,'bts')
    # change_fund('FIL6',4311.75,'bts')
    # change_fund('YOYOW',20000*20+100000,'bts')


    # change_fund('OCT',646516,'eos')
    # change_fund('EOS',44531.000,'eos')

    # change_fund('CYB',572837,'token')
    # change_fund('SEER',14874000,'token')


    # change_fund('ETH',115.37,'hotbit')
    # change_fund('HTB',8597129,'hotbit')



    # 20180904
    # change_fund('OCT',-646000,'eos')
    # change_fund('OCT',572750,'aex')
    # change_fund('YOYOW',405530,'aex')
    # change_fund('CNY',40633,'aex')

    # 20180913 09:39:37
    # 
    # change_fund('YOYOW',-405530,'aex')
    # change_fund('YOYOW',802590,'aex')
    # change_fund('CNY',-40633,'aex')
    # change_fund('OCT',-572750,'aex')
    # change_fund('OCT',554000,'aex')


    # change_fund('EOS',-10590.4645,'bigone')
    # change_fund('USDT',-31197.97,'bigone')

    # change_fund('EOS',12247.59,'bigone')
    # change_fund('USDT',23398.79,'bigone')


    # change_fund('USDT',-43432.73,'huobi')
    # change_fund('USDT',33432.73,'huobi')
    # change_fund('BTS',100000,'huobi')

    # change_fund('CYB',722934.52179-572837,'token')



    # change_fund('USDT',0-33432.73,'huobi')
    # change_fund('eos',8782.24-2723.99,'huobi')

    # change_fund('EOS',14357.26-12247.59,'bigone')
    # change_fund('USDT',11699.68-23398.79,'bigone')

    # 我就当爆仓了
    # change_fund('BTS',-1009017,'bts')
    # change_fund('CNY',233053,'bts')

    # 转入了畅思
    # change_fund('EOS',-14358,'bigone')
    # change_fund('USDT',-11700,'bigone')
    # change_fund('eos',-8782,'huobi')

    # change_fund('EOS',27200,'eos')
    
    is_coin = True

    get_all_amount_all_exchange()

    is_coin = False
    if is_coin:
        get_all_amount_by_exchange()
    else:
        get_all_amount_by_coin()
    return

    # assets_value_sql_s="""
    # -- drop table if exists assets_value;
    # create table if not exists assets_value(
    # id int unsigned primary key auto_increment,
    # name varchar(50) not null,
    # value_int int not null,
    # value_wei tinyint not null,
    # volume bigint not null,
    # create_time int not null
    # );
    # """
    
    # my_assets_sql_s="""
    # -- drop table if exists my_assets;
    # create table if not exists my_assets(
    # id int unsigned primary key auto_increment,
    # name varchar(50) not null,
    # volume int not null,
    # exchange varchar(50) not null,
    # create_time int not null
    # );
    # """

    # mysql_exec_sqls = [assets_value_sql_s,my_assets_sql_s]
    # for sql_s in mysql_exec_sqls:
    #     MYSQL.exec(sql_s)

    # MYSQL.exec('insert into assets_value values(null,"btc",450002212,4,12323445522,null);')
    # save_chat_content('uidxx01','uname1','chat_idxx01','chat_name1','text','content my hh')

# 120.79.41.9
if __name__ == '__main__':
    main()
else:
    MYSQL = Mysql('120.79.41.9','my_blockchain_assets','my_blockchain_assets',db='my_blockchain_assets')
'''
create user "my_blockchain_assets"@"%" identified by "my_blockchain_assets";
grant all privileges on my_blockchain_assets.* to 'my_blockchain_assets'@'%' with grant option;
create database my_blockchain_assets;
'''
