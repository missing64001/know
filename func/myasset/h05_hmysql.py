#!/usr/bin/env python3  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @CreatTime    : 20180516 11:51:47
# @Author  : TIT  
# @File    : TSpase
#  



'''
服务器 120.79.41.9
'''

'''
pip3 install pymysql==0.9.2  /0.7.2/0.7.11
pip uninstall mysql-connector
'''

r'''
数据的备份
mysqldump -uroot -p123456 crawl_proxy  > C:\Users\miss\crawl_proxy.sql
mysql -uroot -p123456 crawl_proxy< C:\Users\miss\crawl_proxy.sql
'''


'''
create user "crawl_proxy"@"%" identified by "crawl_proxy";
grant references,create,select,update,insert on crawl_proxy.* to 'crawl_proxy'@'%' with grant option;
all privileges

create user "my_blockchain_assets"@"%" identified by "my_blockchain_assets";
grant all privileges on my_blockchain_assets.* to 'my_blockchain_assets'@'%' with grant option;
create database my_blockchain_assets;

CREATE DATABASE crawl_proxy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;




create user "evaluateg"@"%" identified by "evaluateg";
grant all privileges on evaluateg.* to 'evaluateg'@'%' with grant option;
CREATE DATABASE evaluateg DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;


'''
'''
field = ('title','uid','power','type','labels','istop','point')
value = (title,uid,power,type,labels,istop,point)
sql_s = MYSQL.insert_s(self.table, value, field)
MYSQL.exec(sql_s)

field = (self.id_name,'title','uid','rnum','cnum','power','type','likenum','labels','istop','point','create_time')
where = 'aid = %s'% aid
other = ''
sql_s = MYSQL.select_s(self.table, field, where,'')
res = MYSQL.get_exec(sql_s,field)

'''
# import mysql

import time,sys,os
# try:
#     import mysql.connector as pym
#     print('mysql.connector')
# except ImportError as e:
#     # print('未开启数据库')
#     import pymysql as pym
#     print('pymysql')
import pymysql as pym
# from mysql.connector.errors import OperationalError
# import mysql.connector.errors.OperationalError as OperationalError

def main():
    MYSQL = Mysql('localhost','test','test',db='test')
    MYSQL.exec('insert into test values();')
    print(MYSQL.get_exec("show variables like '%timeout'"))
    n=20
    while True:
        time.sleep(1)
        n-=1
        print('wait %s seconds' % n,end='\r')
        if n<0:
            break
    MYSQL.exec('insert into test values();')




class Mysql(object):
    """数据库设计成单例模式"""
    def __init__(self,ip,user,password,db=None,port = 3306,charset="utf8",istest=False):
        self.istest =istest
        self.ip = ip
        self.user = user
        self.password = password
        self.db = None
        self.port = port
        self.charset = charset
        # if is_run:
        self.run()
        print(ip,port)
        try:
            self.exec('use %s' % db)
        except Exception:
            self.exec('create database %s;' % db)
            self.exec('use %s;' % db)
        self.db = db
        

    def test(self,*args,**kwargs):
        # self.istest = None
        if self.istest:
            print('    test 命令查看____：\n    ---',*args,**kwargs)

    def insert_s(self,table,value,field=''):
        field = '('+','.join(field) + ')'
        if len(value) == 1:
            value = '("%s")' % str(value[0])
        s = '''insert into {table} {field} values {value} ;'''.format(table=table, field=field ,value=str(value))
        # self.test(s)
        return s

    def select_s(self,table,field,where='',other=''):
        if where:
            # print(where,len(where))
            where = 'where ' + where
        field = ','.join(field)
        s = 'select {field} from {table} {where} {other} ;'.format(table=table, field=field, where=where, other=other)
        # self.test(s)
        return s

    def get_exec(self,s,field=None):
        # print(s)


        try:
            self.cur.execute(s)
        except Exception:
            self.dbserver.ping(reconnect=True)
            self.exec('use %s' % self.db)
            self.cur.execute(s)
        except Exception:
            print('\n------------------------------------------------\nexec_err: ' + s)


        lsts = self.fetch()
        if not field:
            return lsts
        res_lsts = []
        for lst in lsts:
            d = {}
            for i in range(len(lst)):
                ss = field[i]
                if 'unix_timestamp' in field[i]:
                    ss = ss.split('unix_timestamp(')[-1].strip(')')
                d[ss] = lst[i]
            res_lsts.append(d)
        return res_lsts

    def exec(self,s):
        # self.test(s)
        try:
            res = self.cur.execute(s)
            self.commit()
            return self.cur.rowcount
        except Exception:
            print('connect again .............................',s)
            self.dbserver.ping(reconnect=True)
            self.exec('use %s' % self.db)
            res = self.cur.execute(s)
            self.commit()
            return self.cur.rowcount
        except Exception:
            print('\n------------------------------------------------\nexec_err: ' + s)

    def get_max_id(self,table,id_name):
        # sql_s = 'select count({id_name}) from {table}'.format(id_name=id_name,table=table)
        sql_s = 'select {id_name} from {table} order by {id_name} DESC limit 1'.format(id_name=id_name,table=table)
        lst = self.get_exec(sql_s)
        # print(lst)
        return lst[0][0]

    def run(self):
        try:
            self.dbserver = pym.connect(host=self.ip, port=3306, user=self.user, password=self.password, db = self.db, charset='utf8')
        except TypeError:
            self.dbserver = pym.connect(host=self.ip, port=3306, user=self.user, passwd=self.password, db = self.db, charset='utf8')
        self.cur = self.dbserver.cursor()
        if self.db:
            self.cur.execute('use '+ self.db)


    def __enter__(self):
        self.run()
        return self
        

    def __exit__(self,exec_type,exec_value,exec_tb):

        if exec_type is None:
            self.commit();
        else:
            if self.isroolback:
                self.rollback();
            print("退出with时，有异常，类型是", exec_type,
                  "错误是", exec_value)

        self.cur.close()
        self.dbserver.close()


    def commit(self):
        return self.dbserver.commit()

    def rollback(self):
        return self.dbserver.rollback()

    def pfetch(self,n=-1):
        print(self.fetch(n))

    def fetch(self,n=-1):
        '''默认返回所有，或返回n个'''
        if n == -1:
            return self.cur.fetchall()

        elif n > 0:
            return self.cur.fetchmany(n)

if __name__ == '__main__':
    main()