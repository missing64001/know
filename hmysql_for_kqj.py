import sys,os
sys.path.append(r'F:\my\P028_knowledge_system\knowqt\kqj')
os.environ['DJANGO_SETTINGS_MODULE'] ='kqj.settings'
import django 
django.setup()
from data import models
from data.models import Label,Content,HGFile
from django.db.models import Q
from django.utils import timezone