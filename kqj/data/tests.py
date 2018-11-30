


# import sys,os
# sys.path.append('../')
# os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'
# from kqj import settings
# import sys,os
# import django 
# sys.path.append('../')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kqj.settings")
# django.setup()
# from django.conf.urls import url
# from django.contrib import admin





import sys,os
sys.path.append(r'F:\my\P028_knowledge_system\knowqt\kqj')
os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'

# from django.core.management import setup_environ
# from kqj import settings

import django 
django.setup()



from data import models












# Create your tests here.
if __name__ == "__main__":
    print(models.Content.objects.all().count())
    models.Content.objects.create(text='22')