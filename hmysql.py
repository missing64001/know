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
from data.models import Label,Content
from django.db.models import Q
from django.utils import timezone
from django.db import connection
from pprint import pprint
import hashlib
import pickle
from gl.gl import gctdec,tprintex,gcts



label_fields = ('name','pid','queue','grade','create_date')
content_fields = ('name','text','create_date')
get_labels_by_content = {}
get_contents_by_label = {}

class MyModels(object):
    def __init__(self,model=None,obj=None):
        self.model = model
        self.obj = obj
        self.lastcommand = None

    def __getattr__(self,name):
        # print(name)
        if name == 'Label':
            self.model = models.Label
        elif name == 'Content':
            self.model = models.Content
        elif name == 'HGFile':
            self.model = models.HGFile



        elif name == 'DoesNotExist':
            return self.model.DoesNotExist
        elif name not in ('objects','labels'):
            raise ValueError('name:%s is not in default' % name)

        self.lastcommand = name
        return self

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

    def create(self,*args,**kw):
        obj = self.model.objects.create(*args,**kw)
        # return MyModels(self.model,obj)
        return obj

    def labels_add(self,*args,**kw):
        return self.obj.labels.add(*args,**kw)

    def labels_remove(self,*args,**kw):
        return self.obj.labels.remove(*args,**kw)

    def get(self,*args,**kw):
        obj = self.model.objects.get(*args,**kw)
        # return MyModels(self.model,obj)
        return obj

    def save(self):
        return self.obj.save()

    def all(self):
        return self.model.objects.all()

    def filter(self,*args,**kw):
        return self.model.objects.filter(*args,**kw)


def get_models_all_data(obj):
    lst = []
    field_names = None
    if isinstance(obj,models.Label):
        field_names = label_fields
    elif isinstance(obj,models.Content):
        field_names = content_fields
    for name in field_names:
        lst.append(getattr(obj,name))
    return lst


def get_md5(lst):
    m2 = hashlib.md5()
    for l in lst:
        da = str(list(l.items()).sort()).encode('utf-8')
        m2.update(da)
    return m2.hexdigest()


def get_all_data_from_mysql(filename):
    get_labels_by_content = {}
    get_contents_by_label = {}



    labelall = models.Label.objects.all()
    labeldict = {item.id:get_models_all_data(item) for item in labelall}

    contentall = models.Content.objects.all()
    contentdict = {item.id:get_models_all_data(item) for item in contentall}

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
    mymodels = MyModels()

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