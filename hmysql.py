

# 标签
# label
#     id
#     name 可以的名字格式 c_no_xxx
#     pid
#     queue
#     grade
#     create_time

# content
#     id
#     labels
#     text0
#     attachment
#     create_time

# search_history
#     label
#     content
#     create_time
import sys,os
sys.path.append(r'F:\my\P028_knowledge_system\knowqt\kqj')
os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'
import django 
django.setup()
from data import models
from data.models import Label,Content,HGFile
from django.db.models import Q
from django.utils import timezone
from django.db import connection
from pprint import pprint
import hashlib
import pickle
from gl.gl import gctdec,tprintex,gcts,CURRENTURL,open
from threading import Thread,Lock
import threading
from PyQt5.QtCore import QThread,QProcess
import time
import traceback
import inspect
from concurrent.futures import ThreadPoolExecutor
import queue
from functools import wraps
import random
import datetime
from multiprocessing import Process,Pipe
from django.db.utils import OperationalError
from pymysql.err import OperationalError as pe_OperationalError
from socket import timeout


LABEL_FIELDS = ('id','name','pid','queue','grade','create_date')
CONTENT_FIELDS = ('id','name','text','create_date')
HGFILE_FIELDS = ('id','name','path','create_date')
get_labels_by_content = {}
get_contents_by_label = {}
ALLDATA_FILENAME = os.path.join(CURRENTURL,'alldata.dat')
# REPLACE = {}

'''
    函数内部的函数不能通过pickle进行传递 所以多线程的函数需要进行外部定义
'''

def setattr_temp(model,name,value):
    time.sleep(3)
    obj = model.objects.get(id=self.objid)
    return setattr(obj,name,value)

def myModels_labels_add(lid,oid):
    obj = Content.objects.get(id=oid)
    lobj = Label.objects.get(id=lid)
    obj.labels.add(lobj)

def myModels_labels_remove(lid,oid):
    obj = Content.objects.get(id=oid)
    lobj = Label.objects.get(id=lid)
    obj.labels.remove(lobj)







def objsave(model,data):
    obj = model.objects.get(id=data[0])
    if model == Label:
        obj.name = data[LABEL_FIELDS.index('name')]
        obj.pid = data[LABEL_FIELDS.index('pid')]
        obj.queue = data[LABEL_FIELDS.index('queue')]
        obj.grade = data[LABEL_FIELDS.index('grade')]
    elif model == Content:
        obj.name = data[CONTENT_FIELDS.index('name')]
        obj.text = data[CONTENT_FIELDS.index('text')]
    else:
        raise ValueError(str(model) + '错误的参数类型')
    obj.save()



# def model_create(model,id_,*args,**kw):
#     obj = model.objects.create(*args,**kw)
#     self = MyModels(model,None,1)
#     print(id(self.contentdict))
#     a = max(self.contentdict)
#     print(a)

    

#     if isinstance(obj,models.Label):
#         data = self.labeldict.pop(id_)
#         mysql_data = get_model_all_data(obj)
#         data[0] = mysql_data[0]
#         data[-1] = mysql_data[-1]
#         self.labeldict[data[0]] = data

#         if id_ in self.get_contents_by_label:
#             self.get_contents_by_label[data[0]] = self.get_contents_by_label.pop(id_)

#         for labelset in self.get_labels_by_content:
#             for cid in labelset.copy():
#                 if id_ == cid:
#                     labelset.reomve(id_)
#                     labelset.add(data[0])

#     elif isinstance(obj,models.Content):

        
#         data = self.contentdict.pop(id_)
#         mysql_data = get_model_all_data(obj)
#         data[0] = mysql_data[0]
#         data[-1] = mysql_data[-1]
#         self.contentdict[data[0]]

#         if id_ in self.get_labels_by_content:
#             self.get_labels_by_content[data[0]] = self.get_labels_by_content.pop(id_)

#         for contentset in self.get_contents_by_label:
#             for cid in contentset.copy():
#                 if id_ == cid:
#                     contentset.reomve(id_)
#                     contentset.add(data[0])
    # REPLACE.update({id_:obj.id})

def run_for_create(conn1):
    while True:
        try:
            getrecv = conn1.recv()
            if getrecv == 'content395':
                obj = Content.objects.get(id=395)
                conn1.send(obj.text)
            elif getrecv == 'time_connect':
                Content.objects.filter(id=-1)
                conn1.send('bb')

            elif getrecv == 'mysql_all_data':
                mysql_all_data = get_all_data_from_mysql()
                conn1.send(mysql_all_data)
            else:
                create,args,kw = getrecv
                obj = create(*args,**kw)
                data = get_model_all_data(obj)
                conn1.send(data)

        except OperationalError:
            time.sleep(3)
            print('错误 OperationalError')
            print('创建失败进行重启')
            conn1.send('err')
            conn1.close()
            break

        except pe_OperationalError:
            time.sleep(3)
            print('错误 pe_OperationalError')
            print('创建失败进行重启')
            conn1.send('err')
            conn1.close()
            break

        except ConnectionResetError:
            time.sleep(3)
            print('错误 ConnectionResetError')
            print('创建失败进行重启')
            conn1.send('err')
            conn1.close()
            break

        except timeout:
            time.sleep(3)
            print('错误 timeout')
            print('创建失败进行重启')
            conn1.send('err')
            conn1.close()
            break

        except Exception:
            traceback.print_exc()
            time.sleep(3)
            print('创建失败进行重启')
            conn1.send('err')
            conn1.close()
            break

class ConnThread_for_create(QThread):
    def __init__(self):
        super().__init__()
        self.que = queue.Queue()
        self.queres = queue.Queue()
        self.isrun = False

    def run(self):
        self.isrun = True
        model = None
        args = None
        queget = None
        while True:
            conn1, self.conn = Pipe()
            Process(target=run_for_create,args = (conn1,)).start()
            conn1.close()
            if queget:
                self.que.put(queget)
                # print('出现错误')
            while True:
                queget = self.que.get()
                if queget in ('content395','mysql_all_data','time_connect'):
                    self.conn.send(queget)
                    data = self.conn.recv()
                    if data == 'err':
                        break
                    else:
                        self.queres.put(data)
                else:
                    model,args = queget
                    self.conn.send(args)
                    data = self.conn.recv()
                    if data == 'err':
                        break
                    else:
                        if model == models.Label:
                            self.mself.labeldict[data[0]] = data
                            res = MyModels(model,None,data[0])
                        elif model == models.Content:
                            self.mself.contentdict[data[0]] = data
                            res = MyModels(model,None,data[0])
                        elif model == models.HGFile:
                            res = data[0]
                        
                        self.queres.put(res)

            self.conn.close()

    def set_mself(self,mself):
        self.mself = mself



# class Job(threading.Thread):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__flag = threading.Event()     # 用于暂停线程的标识
#         self.__flag.set()       # 设置为True
#         self.__running = threading.Event()      # 用于停止线程的标识
#         self.__running.set()      # 将running设置为True

#     def run(self,lst):
#         while self.__running.isSet():
#             self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
#             print (time.time())
#             time.sleep(1)

#     def pause(self):
#         self.__flag.clear()     # 设置为False, 让线程阻塞

#     def resume(self):
#         self.__flag.set()    # 设置为True, 让线程停止阻塞

#     def stop(self):
#         self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
#         self.__running.clear()        # 设置为False 


# 选择哪个运行 后期可以实现 多线程发送
def whichrun(self,f1,f2,mustrun=True):
    if len(f1) == 2:
        f1 = (*f1,{})

    if len(f2) == 2:
        f2 = (*f2,{})

    re1 = f1[0](*f1[1],**f1[2])
    if mustrun:
        self.mself.conn.send(f2)

    return re1

# 多线程
def run(conn1):
    global QUE
    global RUNN_ALIVE
    # f2,re1 = lst
    while True:
        f2 = QUE.get()

        try:
            end = '\n' if QUE.qsize() > 5 else '\r'
            print('未完成数量',QUE.qsize(),'运行中。。。',end=end)
            # f2 = (f2[0],tuple([ REPLACE.get(i,i) if type(i) == int else i  for i in f2[1]]),f2[2])

            # for i in f2[1]:
            #     if type(i) == int and i >= 999000000000 and f2[0] != model_create:
            #         raise ValueError('f2的参数出错 %s' % str(f2))

            re2 = f2[0](*f2[1],**f2[2])
            print('运行完成   ',end='\r')
        # except OperationalError as e:
        except Exception as e:

            if type(e) != OperationalError:
                traceback.print_exc()
                print('错误类型',type(e))
            print('出错了，并对数据进行备份')
            RUNN_ALIVE = False

            lst = []
            lst.append(f2)
            while not QUE.empty():
                lst.append(QUE.get())

            filename = os.path.join(CURRENTURL,'gl','errbak.dat')
            with open(filename,'wb') as f:
                pickle.dump(lst,f)
                # pickle.dump(REPLACE,f)
            
            print('3秒后重新启动mysql处理')
            time.sleep(3)
            print('重新启动mysql')
            conn1.send('err')
            conn1.close()
            RUNN_ALIVE = False
            break



# 多进程接受
def runn(conn1,conn2,lst):
    # REPLACE.update(replace)
    conn2.close()
    global QUE
    global RUNN_ALIVE
    RUNN_ALIVE = True
    QUE = queue.Queue()
    for l in lst:
        QUE.put(l)

    t1 = Thread(target=run,args=(conn1,))
    t1.start()
    while RUNN_ALIVE:
        try:
            msg = conn1.recv()
        except EOFError:
            break
        QUE.put(msg)
        if not t1.isAlive():
            t1 = Thread(target=run,args=(conn1,))
            t1.start()

    
    




# class Thread(Process):
#     # def __init __(self):
#     #     super(Thread，self).__ init __()
#     def run(self):
#         print(1111111111111111111)
#         i = 0
#         import time
#         filename = '11xx2233.txt'
#         with open(filename,'a',encoding='utf-8') as f:
            
#             while True:
#                 time.sleep(1)
#                 i += 1
#                 print('-----------',i)
#                 f.write(str(i))
#                 f.write('\n')





def getattr_data(di,fields,objid,name):
    return di[objid][fields.index(name)]

def setattr_data(di,fields,objid,name,value):
    di[objid][fields.index(name)] = value




class MyModels(object):
    all_data = []
    mysql_data = []
    local_data = []
    ThreadCreate = ConnThread_for_create()

    def __init__(self,model=None,obj=None,objid=None):
        self.model = model
        self.obj = obj
        if objid:
            self.objid = objid
        elif obj:
            self.objid = obj.id
        else:
            self.objid = objid

        self.lastcommand = None
        

        self.labeldict = None
        self.contentdict = None
        self.get_labels_by_content = None
        self.get_contents_by_label = None

        if not self.ThreadCreate.isrun:
            self.ThreadCreate.set_mself(self)
            self.ThreadCreate.start()

        self.get_data()

    def __getattr__(self,name):
        # print(name)
        if name == 'Label':
            self.model = models.Label
        elif name == 'Content':
            self.model = models.Content
        elif name == 'HGFile':
            self.model = models.HGFile


        elif self.model == models.Label and name in LABEL_FIELDS:
            fields = LABEL_FIELDS
            di = self.labeldict
            objid = self.objid

            re1 = (getattr_data,(di,fields,objid,name))
            re2 = (getattr,(self.obj,name))
            return whichrun(self,re1,re2,False)
        elif self.model == models.Content and name in CONTENT_FIELDS:
            fields = CONTENT_FIELDS
            di = self.contentdict
            objid = self.objid

            re1 = (getattr_data,(di,fields,objid,name))
            re2 = (getattr,(self.obj,name))
            return whichrun(self,re1,re2,False)
        elif self.model == models.HGFile and name in HGFILE_FIELDS:
            return getattr(self.obj,name)


        elif name == 'DoesNotExist':
            return self.model.DoesNotExist

        # elif name in ('__name__',):
        #     super().__name__

        elif name not in ('objects','labels'):
            raise ValueError('name:%s is not in default' % name)

        self.lastcommand = name
        return self

    def __setattr__(self,name,value):
        # set数据不需要保存的原因是 最后通过save进行保存

        if name in ('model','obj','lastcommand','labeldict','contentdict','get_labels_by_content','get_contents_by_label'):
            super().__setattr__(name,value)
        #     return

        di = None
        if self.model == models.Label and name in LABEL_FIELDS:
            di = self.labeldict
            fields = LABEL_FIELDS
            objid = self.objid

            re1 = (setattr_data,(di,fields,objid,name,value))


            re2 = (setattr_temp,(Label,objid,name,value))
            return whichrun(self,re1,re2,False)


        elif self.model == models.Content and name in CONTENT_FIELDS:
            di = self.contentdict
            fields = CONTENT_FIELDS
            objid = self.objid

            re1 = (setattr_data,(di,fields,objid,name,value))


            re2 = (setattr_temp,(Content,objid,name,value))
            return whichrun(self,re1,re2,False)

        elif self.model == models.HGFile and name in HGFILE_FIELDS:
            setattr(self.obj,name,value)
            return

        else:
            return super().__setattr__(name,value)

    def get_data(self):
        if not self.all_data:
            all_data = get_all_data_from_mysql()
            if os.path.exists(ALLDATA_FILENAME):
                loacal_all_data = get_all_data_from_local()
                if get_md5(all_data) != get_md5(loacal_all_data):

                    get_md5_bj(all_data,loacal_all_data)
                    print(get_md5(all_data))
                    print(get_md5(loacal_all_data))
                    print('数据不一致保存到了', save_all_data(*all_data,True))
                    # raise ValueError('mysql data different from local data')
                    # all_data = loacal_all_data
                    self.mysql_data.append(all_data[0])
                    self.mysql_data.append(all_data[1])
                    self.mysql_data.append(all_data[2])
                    self.mysql_data.append(all_data[3])

                    self.local_data.append(loacal_all_data[0])
                    self.local_data.append(loacal_all_data[1])
                    self.local_data.append(loacal_all_data[2])
                    self.local_data.append(loacal_all_data[3])
                else:
                    print('数据一致性验证完毕')
            else:
                loacal_all_data = all_data
                print('未获得本地数据')

            self.all_data.append(loacal_all_data[0])
            self.all_data.append(loacal_all_data[1])
            self.all_data.append(loacal_all_data[2])
            self.all_data.append(loacal_all_data[3])

        self.labeldict,self.contentdict,self.get_labels_by_content,self.get_contents_by_label = self.all_data

    def check_data(self):
        print('get_mysql_all_data...',end = '\r')
        self.ThreadCreate.que.put('mysql_all_data')
        all_data = self.ThreadCreate.queres.get()
        print('get_mysql_all_data完成',end = '\r')


        # all_data = get_all_data_from_mysql()
        if os.path.exists(ALLDATA_FILENAME):
            loacal_all_data = get_all_data_from_local()
            if get_md5(all_data) != get_md5(loacal_all_data):

                get_md5_bj(all_data,loacal_all_data)
                print(get_md5(all_data))
                print(get_md5(loacal_all_data))
                print('数据不一致保存到了')
            else:
                print('数据一致性验证完毕')
                return True
        else:
            loacal_all_data = all_data
            print('未获得本地数据')

    def add(self,*args,**kw):
        if not self.lastcommand:
            raise ValueError('lastcommand is None,can\'t add')
        addfun = getattr(self,'%s_add' % self.lastcommand)
        return addfun(*args,**kw)

    def remove(self,*args,**kw):
        if not self.lastcommand:
            raise ValueError('lastcommand is None,can\'t remove')
        removefun = getattr(self,'%s_remove' % self.lastcommand)
        return removefun(*args,**kw)

    def all(self,*args,**kw):
        if not self.lastcommand:
            raise ValueError('lastcommand is None,can\'t remove')
        allfun = getattr(self,'%s_all' % self.lastcommand)
        return allfun(*args,**kw)

    def labels_add(self,label):
        def _labels_add(label):
            objid = self.objid
            if hasattr(label,'objid'):
                labelid = label.objid
            else:
                labelid = label.id

            labelset = self.get_labels_by_content.get(objid)
            if labelset:
                labelset.add(labelid)
            else:
                self.get_labels_by_content[objid] = {labelid}

            contentset = self.get_contents_by_label.get(labelid)
            if contentset:
                contentset.add(objid)
            else:
                self.get_contents_by_label[labelid] = {objid}

        re1 = (_labels_add,(label,))
        re2 = (myModels_labels_add,(label.objid,self.objid))
        return whichrun(self,re1,re2)

    def labels_remove(self,label):

        def _labels_remove(label):
            objid = self.objid
            if hasattr(label,'objid'):
                labelid = label.objid
            else:
                labelid = label.id

            labelset = self.get_labels_by_content.get(objid)
            if labelset and labelid in labelset:
                    labelset.remove(labelid)
            else:
                self.get_labels_by_content[objid] = {labelid}

            contentset = self.get_contents_by_label.get(labelid)
            if contentset and objid in contentset:
                    contentset.remove(objid)
            else:
                self.get_contents_by_label[labelid] = {objid}

        re1 = (_labels_remove,(label,))
        re2 = (myModels_labels_remove,(label.objid,self.objid))
        return whichrun(self,re1,re2)

    def create(self,*args,**kw):

        # def model_create(self,*args,**kw):


        # return model_create(self,*args,**kw)

        print('新建item中...',end = '\r')
        self.ThreadCreate.que.put((self.model,(self.model.objects.create,args,kw)))
        data = self.ThreadCreate.queres.get()
        print('新建item完成',end = '\r')

        return data

    def get_content395(self):

        print('get_content395...',end = '\r')
        self.ThreadCreate.que.put('content395')
        data = self.ThreadCreate.queres.get()
        print('get_content395完成',end = '\r')
        return data

    def time_connect(self):
        print('创建mysql连接中。。',end='\r')
        self.ThreadCreate.que.put('time_connect')
        data = self.ThreadCreate.queres.get()
        print('创建mysql连接完成  ',end='\r')

    def save(self):
        re1 = (lambda:None,())
        if self.model == Label:
            re2 = (objsave,(Label,self.labeldict[self.objid]))
        elif self.model == Content:
            re2 = (objsave,(Content,self.contentdict[self.objid]))
        return whichrun(self,re1,re2)

    def filter_cid_by_textlst(self,lst):
        resset = set()
        for i,content in self.contentdict.values():
            name = content[CONTENT_FIELDS.index('name')]
            text = content[CONTENT_FIELDS.index('text')]
            for te in lst:
                if te not in name and te not in text:
                    break
            else:
                resset.add(i)
        return resset

    def labels_all(self,*args,**kw):
        data = self.obj.labels.all(*args,**kw)

        print('------------------------')
        for ins in inspect.stack():
            print('%s \n lineno:%s  --  %s'%(ins.filename,ins.lineno,''.join(ins.code_context).strip()))

        return MyQuery(data)

    def objects_all(self,*args,**kw):
        data = self.model.objects.all(*args,**kw)
        
        print('------------------------')
        for ins in inspect.stack():
            print('%s \n lineno:%s  --  %s'%(ins.filename,ins.lineno,''.join(ins.code_context).strip()))

        return MyQuery(data)

    def get(self,*args,**kw):
        obj = self.model.objects.get(*args,**kw)
        
        print('------------------------')
        for ins in inspect.stack():
            print('%s \n lineno:%s  --  %s'%(ins.filename,ins.lineno,''.join(ins.code_context).strip()))

        obj = MyModels(self.model,obj)
        return obj

    def filter(self,*args,**kw):
        data = self.model.objects.filter(*args,**kw)
        
        if kw != {'id':-100}:
            print('------------------------')
            for ins in inspect.stack():
                print('%s \n lineno:%s  --  %s'%(ins.filename,ins.lineno,''.join(ins.code_context).strip()))

        return MyQuery(data)


class MyQuery(object):
    """docstring for myquery
        MyModels(__class__,None,id)
        MyModels(__class__,obj)

        MyQuery(query)
        MyQuery(dict,model)
    """

    def __init__(self, query, model=None):
        self.query = query
        self.model = model


    def __iter__(self):
        if self.model:
            self.objs = list(self.query)
        else:
            self.objs = list(self.query)
        self.index = 0
        self.maxindex = len(self.objs)
        return self

    def __next__(self):
        if self.index >= self.maxindex:
            raise StopIteration
        else:
            obj = self.objs[self.index]
            self.index+=1
            if self.model:
                return MyModels(self.model,None,obj)
            return MyModels(obj.__class__,obj)

            

    def values(self,*args,**kw):
        return self.query.values(*args,**kw)

    def order_by(self,*args,**kw):
        return MyQuery(self.query.order_by(*args,**kw))
        


def get_model_all_data(obj):
    lst = []
    field_names = None
    if isinstance(obj,models.Label):
        field_names = LABEL_FIELDS
    elif isinstance(obj,models.Content):
        field_names = CONTENT_FIELDS
    elif isinstance(obj,models.HGFile):
        return [obj.id]
    for name in field_names:
        lst.append(getattr(obj,name))
    return lst


def get_md5(lst):
    m2 = hashlib.md5()
    for l in lst:
        ll = list(l.items())
        ll.sort()
        if ll and type(ll[0][1]) == set:
            ll = [ (i[0],sorted(list(i[1]))) for i in ll]
        da = str(ll).encode('utf-8')
        # print(len(da))
        m2.update(da)
    return m2.hexdigest()

def get_md5_bj_old(lst1,lst2):
    m1 = hashlib.md5()
    m2 = hashlib.md5()

    print('get_md5_bj be')
    for l1,l2 in zip(lst1,lst2):
        ll1 = list(l1.items())
        ll1.sort()
        if ll1 and type(ll1[0][1]) == set:
            ll1 = [ (i[0],sorted(list(i[1]))) for i in ll1]
        da1 = str(ll1).encode('utf-8')
        m1.update(da1)
        print(m1.hexdigest())

        ll2 = list(l2.items())
        ll2.sort()
        if ll2 and type(ll2[0][1]) == set:
            ll2 = [ (i[0],sorted(list(i[1]))) for i in ll2]
        da2 = str(ll2).encode('utf-8')
        m2.update(da2)
        print(m2.hexdigest())

    print('get_md5_bj end')

def get_md5_bj(lst1,lst2):
    # all_data,loacal_all_data
    res = []
    show_id = (set(),set())
    for i,l1,l2 in zip([0,1,2,3],lst1,lst2):
        r = []
        setl1 = set(l1) - set(l2)
        setl2 = set(l2) - set(l1)
        setl3 = set(l2) & set(l1)

        for s in setl1:
            r.append([[s,l1[s]],['XXXXXX空白没有数据XXXXXXX']])
            if i == 2:
                show_id[1].add(s)
                show_id[0].update(l1[s])
            elif i == 3:
                show_id[0].add(s)
                show_id[1].update(l1[s])

        for s in setl2:
            if l2[s] == set():
                print(s)
                del l2[s]
                continue

            r.append([['XXXXXX空白没有数据XXXXXXX'],[s,l2[s]]])
            if i == 2:
                show_id[1].add(s)
                show_id[0].update(l2[s])
            elif i == 3:
                show_id[0].add(s)
                show_id[1].update(l2[s])

        for s in setl3:
            if l1[s] != l2[s]:
                r.append([[s,l1[s]],[s,l2[s]]])
                if i == 2:
                    show_id[1].add(s)
                    show_id[0].update(l1[s])
                elif i == 3:
                    show_id[0].add(s)
                    show_id[1].update(l1[s])

        res.append(r)
    pprint(res)

def randomstr(n):
    src = str(time.time())
    m2 = hashlib.md5()   
    m2.update(src.encode())  
    return ''.join(random.sample(m2.hexdigest(),10))


    pprint(res)
    print(show_id)


    print('labels:')
    for i in show_id[0]:
        print('   ',i,lst1[0][i][1])


    print('contents:')
    for i in show_id[1]:
        print('   ',i,lst1[1][i][1])
    return res

def get_all_data_from_mysql():
    get_labels_by_content = {}
    get_contents_by_label = {}



    labelall = models.Label.objects.all()
    labeldict = {item.id:get_model_all_data(item) for item in labelall}

    contentall = models.Content.objects.all()
    contentdict = {item.id:get_model_all_data(item) for item in contentall}

    cursor = connection.cursor()
    sql = 'select content_id,label_id from data_content_labels;'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        labels_set = get_labels_by_content.get(row[0])
        if not labels_set:
            get_labels_by_content[row[0]] = {row[1]}
        else:
            labels_set.add(row[1])

        contents_set = get_contents_by_label.get(row[1])
        if not contents_set:
            get_contents_by_label[row[1]] = {row[0]}
        else:
            contents_set.add(row[0])
    print('finish get_all_data_from_mysql')
    # print(get_md5((labeldict,contentdict,get_labels_by_content,get_contents_by_label)))
    return labeldict,contentdict,get_labels_by_content,get_contents_by_label



def get_all_data_from_local():
    with open(ALLDATA_FILENAME,'rb') as f:
        labeldict = pickle.load(f)
        contentdict = pickle.load(f)
        get_labels_by_content = pickle.load(f)
        get_contents_by_label = pickle.load(f)
    return labeldict,contentdict,get_labels_by_content,get_contents_by_label

def save_all_data(labeldict,contentdict,get_labels_by_content,get_contents_by_label,isnow=False):
    filename = ALLDATA_FILENAME
    if isnow:
        time_now_str = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
        filename += time_now_str
    with open(filename,'wb') as f:
        pickle.dump(labeldict,f)
        pickle.dump(contentdict,f)
        pickle.dump(get_labels_by_content,f)
        pickle.dump(get_contents_by_label,f)

    return filename

def main():
    q = queue.Queue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print (q.get())






    # from django.db.utils import OperationalError
    # # from pymysql.err import OperationalError
    # while True:
    #     input()
    #     try:
    #         x = models.Content.objects.get(id=3)
    #         print(x)
    #     except OperationalError as e:
    #         traceback.print_exc()

    #     except:
    #         print('new')
    #         traceback.print_exc()
    
def set_local_data_to_mysql():
    # m = MyModels()
    # m.get_data()
    all_data = get_all_data_from_mysql()
    loacal_all_data = get_all_data_from_local()
    res = get_md5_bj(all_data,loacal_all_data)
    labeldict,contentdict,get_labels_by_content,get_contents_by_label = loacal_all_data
    # pprint(res[0])
    labels = []
    contents = []
    lc = []

    for rs in res[:1]:
        for r in rs:
            labels.append(r[0][0])
            # print(r[0][0])
    print(labels)
    for l in labels:
        obj = Label.objects.get(id=l)
        obj.name = labeldict[l][LABEL_FIELDS.index('name')]
        obj.pid = labeldict[l][LABEL_FIELDS.index('pid')]
        obj.queue = labeldict[l][LABEL_FIELDS.index('queue')]
        obj.grade = labeldict[l][LABEL_FIELDS.index('grade')]
        obj.save()


    for rs in res[1:2]:
        for r in rs:
            contents.append(r[0][0])
    print(contents)
    for i in contents:
        obj = Content.objects.get(id=i)
        obj.name = contentdict[i][CONTENT_FIELDS.index('name')]
        obj.text = contentdict[i][CONTENT_FIELDS.index('text')]
        obj.save()

    for rs in res[2:3]:
        for r in rs:
            lc.append(r[1][0])
    print(lc)
    for i in lc:
        local_labelset = loacal_all_data[2].get(i,set())
        mysql_labelset = all_data[2].get(i,set())
        adds = local_labelset - mysql_labelset
        dels = mysql_labelset - local_labelset
        # cobj = MyModels(Content,None,i)
        cobj = Content.objects.get(id=i)
        for add_ in adds:
            cobj.labels.add(Label.objects.get(id=add_))
        for del_ in dels:
            cobj.labels.remove(Label.objects.get(id=del_))




# C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Lib\site-packages\pymysql\connections.py
# 744  - self.ping



# objsave = 3
if __name__ == '__main__':
    main()
    # set_local_data_to_mysql()
else:
    # mymodels = MyModels()
    pass

# def gettype(obj):
#     if isinstance(obj, models.Label):
#         return 'l'
#     elif isinstance(obj, models.Content):
#         return 'c'
#     print(obj,'错误的参数类型')
#     return

# x = models.Label.objects.filter(id=3)[0]
# print(gettype(x))
# 
# print(x)
# print(models.Label.objects.create('222',3,4,5,6,7,8,9,0,1,1,2,2,3,4,5,6,7,aa=33,bb=33,cc=11))
# x.grade = 3
# print('zzz')
# x.grade = 5
# x.name = '''中国'sdf''\nw''ef""'''
# print('hhh')
# x.save()
# print('ccc')

# x = models.Label.objects.filter(id=3)[0]
# print('aaa')

        # cobj = models.Content.objects.create(name=name,text=text)
        # cobj.labels.add(label)