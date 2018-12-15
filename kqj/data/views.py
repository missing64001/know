from django.shortcuts import render
import sys,os
CURRENTURL = os.path.dirname(__file__)
path = os.path.dirname(CURRENTURL)
path = os.path.dirname(path)
sys.path.insert(1,path)

from django.http import HttpResponse
import json
import qt
from .models import *

# sys.path.insert(1,path)

# Create your views here.


def tree_view(request):
    # mw = qt.Mainwindow()
    # mw.le1.setText('#1')
    # mw.search_models()
    return render(request,'tree.html')


def getdata_view(request):

    search = request.GET.get('search')
    cid = request.GET.get('cid')
    ctype = request.GET.get('ctype')
    if search:
        textlst = search.strip().split(' ')

        qgetdata = qt.getdata()
        qgetdata.set_all_data()
        content_id_set_by_text,label_id_set = qgetdata.get_contents_by_textlst(textlst)
        res = qgetdata.set_label_treeitems(label_id_set)
        qgetdata.set_contents(res,content_id_set_by_text)

        res = json.dumps(res)
    elif cid and ctype:
        cid = int(cid)
        cobj = Content.objects.get(id=cid)
        res = cobj.text


    return HttpResponse(res)



