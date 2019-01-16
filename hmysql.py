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
#     text
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
from django.db.models import Q
from django.utils import timezone





x = models.Label.objects.filter(id=3)[0]
print(x)

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