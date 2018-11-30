# import sys,os
# sys.path.append(r'F:\my\P028_knowledge_system\knowqt\kqj')
# os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'
# import django 
# django.setup()
# from data import models
# from django.db.models import Q

print('本地try_command.py')
import sys,os
import traceback
import time

sys.path.append(r'F:\mygit\python\evaluate')
os.environ['DJANGO_SETTINGS_MODULE'] ='evaluateg.settings'
import django 
try:
    django.setup()
    filename = 'F:\\my\\P028_knowledge_system\\knowqt\\myfn\\h10_try_command_file.txt'
    with open(filename,'r',encoding='utf-8') as f:
        data = f.read()
    print(data)
    os.system(data)
except:
    traceback.print_exc()
# 


input('点击回车结束')


# import sys,os
# sys.path.append(r'F:\my\P028_knowledge_system\knowqt\kqj')
# os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'
# import django 
# django.setup()