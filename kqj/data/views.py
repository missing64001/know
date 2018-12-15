from django.shortcuts import render
import sys,os
CURRENTURL = os.path.dirname(__file__)
path = os.path.dirname(CURRENTURL)
path = os.path.dirname(path)
sys.path.insert(1,path)

from django.http import HttpResponse
import json
import re
import qtdata as qt
from .models import *

from pprint import pprint

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



def xs_view(request):
    directory = os.path.dirname(os.path.dirname(CURRENTURL))
    directory = os.path.join(directory,'func','xiaoshuo','day')

    xsdict = {}
    for curdir,subdirs,files in os.walk(directory):
        for file in files:
            res = re.findall(r'\d+ (.+?)(\d+) (.+?).txt',file)
            if res:
                res = res[0]
                lst = xsdict.get(res[0])
                if lst:
                    lst.append((int(res[1]),res[2],os.path.join(curdir,file)))
                else:
                    xsdict[res[0]] = [(int(res[1]),res[2],os.path.join(curdir,file))]

        break

    # pprint(xsdict)
    last20 = {}
    for name,lst in xsdict.items():
        lst.sort(key=lambda x:x[0])
        last20[name] = lst[-20:]



    return render(request,'xiaoshuo.html',{'xss':last20.items()})

def getxsdata_view(request):
    directory = os.path.dirname(os.path.dirname(CURRENTURL))
    directory = os.path.join(directory,'func','xiaoshuo','day')

    xsdict = {}
    for curdir,subdirs,files in os.walk(directory):
        for file in files:
            res = re.findall(r'\d+ (.+?)(\d+) (.+?).txt',file)
            if res:
                res = res[0]
                xsdict[res[0] + str(int(res[1]))] = os.path.join(curdir,file)
    filename = xsdict[request.GET.get('name')]
    with open(filename,'r') as f:
        data = f.read()
    data = '\n'.join([da.strip() for da in data.split('\n') if da.strip()])
    return render(request,'xsdata.html',{'data':data})