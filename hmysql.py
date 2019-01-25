
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
from gl.gl import gctdec,tprintex,gcts
from threading import Thread
from PyQt5.QtCore import QThread,QProcess
import time

LABEL_FIELDS = ('id','name','pid','queue','grade','create_date')
CONTENT_FIELDS = ('id','name','text','create_date')
HGFILE_FIELDS = ('id','name','path','create_date')
get_labels_by_content = {}
get_contents_by_label = {}



def run(lst):
    while True:
        if lst:
            s = lst.pop()
            print(s,len(lst))
            time.sleep(1)
        time.sleep(0.1)

def runn(conn1,conn2):
    conn2.close()
    lst = []
    Thread(target=run,args=(lst,)).start()
    while True:
        try :
            msg = conn1.recv()
            lst.append(msg)
        except EOFError:  #抛出无数据时异常
            conn1.close()
            break



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

# 选择哪个运行 后期可以实现
def whichrun(f1,f2,mustrun=True):
    re1 = f1[0](*f1[1])
    if mustrun:
        re2 = f2[0](*f2[1])
    else:
        return re1
    if re1 != re2:
        print('re1 != re2',re1,re2)
    else:
        print('运行了whichrun' ,end='\r')
    return re2

class MyModels(object):
    all_data = []
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
            return whichrun(re1,re2,False)
        elif self.model == models.Content and name in CONTENT_FIELDS:
            fields = CONTENT_FIELDS
            di = self.contentdict
            objid = self.objid

            re1 = (getattr_data,(di,fields,objid,name))
            re2 = (getattr,(self.obj,name))
            return whichrun(re1,re2,False)
        elif self.model == models.HGFile and name in HGFILE_FIELDS:
            return getattr(self.obj,name)


        elif name == 'DoesNotExist':
            return self.model.DoesNotExist
        elif name not in ('objects','labels'):
            raise ValueError('name:%s is not in default' % name)

        self.lastcommand = name
        return self

    def __setattr__(self,name,value):


        if name in ('model','obj','lastcommand','labeldict','contentdict','get_labels_by_content','get_contents_by_label'):
            super().__setattr__(name,value)
        #     return

        di = None
        if self.model == models.Label and name in LABEL_FIELDS:
            di = self.labeldict
            fields = LABEL_FIELDS
            objid = self.objid

            re1 = (setattr_data,(di,fields,objid,name,value))

            def _temp(self,name,value):
                obj = self.obj
                if not obj:
                    obj = self.model.objects.get(id=self.objid)
                    self.obj = obj
                return setattr(obj,name,value)
            re2 = (_temp,(self,name,value))
            return whichrun(re1,re2)


        elif self.model == models.Content and name in CONTENT_FIELDS:
            di = self.contentdict
            fields = CONTENT_FIELDS
            objid = self.objid

            re1 = (setattr_data,(di,fields,objid,name,value))

            def _temp(self,name,value):
                obj = self.obj
                if not obj:
                    obj = self.model.objects.get(id=self.objid)
                    self.obj = obj
                return setattr(obj,name,value)
            re2 = (_temp,(self,name,value))
            return whichrun(re1,re2)

        elif self.model == models.HGFile and name in HGFILE_FIELDS:
            setattr(self.obj,name,value)
            return

        else:
            return super().__setattr__(name,value)
        


        

    def get_data(self):
        if not self.all_data:
            filename = 'alldata.dat'
            all_data = get_all_data_from_mysql(filename)
            self.all_data.append(all_data[0])
            self.all_data.append(all_data[1])
            self.all_data.append(all_data[2])
            self.all_data.append(all_data[3])

        self.labeldict,self.contentdict,self.get_labels_by_content,self.get_contents_by_label = self.all_data

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

        def labels_add(label):
            if label.obj:
                lobj = label.obj
            else:
                lobj = Label.objects.get(id=label.objid)
            self.obj.labels.add(lobj)



        re1 = (_labels_add,(label,))
        re2 = (labels_add,(label,))
        return whichrun(re1,re2)

    def labels_remove(self,label):

        def _labels_remove(label):
            objid = self.objid
            if hasattr(label,'objid'):
                labelid = label.objid
            else:
                labelid = label.id

            labelset = self.get_labels_by_content.get(objid)
            if labelset:
                labelset.remove(labelid)
            else:
                self.get_labels_by_content[objid] = {labelid}

            contentset = self.get_contents_by_label.get(labelid)
            if contentset:
                contentset.remove(objid)
            else:
                self.get_contents_by_label[labelid] = {objid}

        def labels_remove(label):
            if label.obj:
                lobj = label.obj
            else:
                lobj = Label.objects.get(id=label.objid)
            self.obj.labels.remove(lobj)

        re1 = (_labels_remove,(label,))
        re2 = (labels_remove,(label,))
        return whichrun(re1,re2)

    def create(self,*args,**kw):
        obj = self.model.objects.create(*args,**kw)

        if isinstance(obj,models.Label):
            self.labeldict[obj.id] = get_model_all_data(obj)
        elif isinstance(obj,models.Content):
            self.contentdict[obj.id] = get_model_all_data(obj)

        return MyModels(self.model,obj)

    def save(self):
        re1 = (lambda:None,())
        re2 = (self.obj.save,())
        return whichrun(re1,re2)

    def labels_all(self,*args,**kw):
        data = self.obj.labels.all(*args,**kw)
        return MyQuery(data)

    def objects_all(self,*args,**kw):
        data = self.model.objects.all(*args,**kw)
        return MyQuery(data)

    def get(self,*args,**kw):
        obj = self.model.objects.get(*args,**kw)
        obj = MyModels(self.model,obj)
        return obj

    def filter(self,*args,**kw):
        data = self.model.objects.filter(*args,**kw)
        return MyQuery(data)


class MyQuery(object):
    """docstring for myquery"""
    def __init__(self, query):
        self.query = query


    def __iter__(self):
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
    for name in field_names:
        lst.append(getattr(obj,name))
    return lst


def get_md5(lst):
    m2 = hashlib.md5()
    for l in lst:
        ll = list(l.items())
        ll.sort()
        da = str(ll).encode('utf-8')
        # print(len(da))
        m2.update(da)
    return m2.hexdigest()


def get_all_data_from_mysql(filename):
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
    print(get_md5((labeldict,contentdict,get_labels_by_content,get_contents_by_label)))
    return labeldict,contentdict,get_labels_by_content,get_contents_by_label



def get_all_data_from_local(filename):
    with open(filename,'rb') as f:
        labeldict = pickle.load(f)
        contentdict = pickle.load(f)
        get_labels_by_content = pickle.load(f)
        get_contents_by_label = pickle.load(f)
    return labeldict,contentdict,get_labels_by_content,get_contents_by_label

def save_all_data(filename,labeldict,contentdict,get_labels_by_content,get_contents_by_label):
    with open(filename,'wb') as f:
        pickle.dump(labeldict,f)
        pickle.dump(contentdict,f)
        pickle.dump(get_labels_by_content,f)
        pickle.dump(get_contents_by_label,f)


def main():
    x = models.Content.objects.get(id=3)
    print(x)
    print(getattr(x,'pk'))
    pprint(dir(x))
    # for name in dir(x):
    #     print(name,getattr(x,name))
    # print(list(x))
    

    exit()








    filename = 'alldata.dat'
    gcts(22)
    all_data = get_all_data_from_local(filename)
    gcts(len(all_data),True)

    # all_data = get_all_data_from_mysql(filename)

    md5 = get_md5(all_data)
    gcts(md5)
    print(md5)
    tprintex()
    # save_all_data(filename,*all_data)






    # pprint(get_labels_by_content)

    
if __name__ == '__main__':
    main()
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