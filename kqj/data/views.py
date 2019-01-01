from django.shortcuts import render
import sys,os
CURRENTURL = os.path.dirname(__file__)
path = os.path.dirname(CURRENTURL)
path = os.path.dirname(path)
sys.path.insert(1,path)

from django.http import HttpResponse,HttpResponseRedirect
import json
import re
import qtdata as qt
from .models import *

from pprint import pprint
from .myasset.get_asset_data import getres
from .myasset.get_other_data import get_wal_data

# sys.path.insert(1,path)

# Create your views here.


def tree_view(request):
    if not get_user_group(request.user,'super'):
        return HttpResponseRedirect('/admin/login/?next=/')
    return render(request,'tree.html')


def getdata_view(request):
    if not get_user_group(request.user,'super'):
        return HttpResponse(0)

    search = request.GET.get('search')
    cid = request.GET.get('cid')
    ctype = request.GET.get('ctype')
    txt = request.GET.get('txt')
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
    elif txt:
        cobj = Content.objects.get(id=395)
        cobj.text = cobj.text + '\n%s' % txt
        cobj.save()
        res = 'txt'

    return HttpResponse(res)



def xs_view(request):
    if not get_user_group(request.user,'super'):
        return HttpResponseRedirect('/admin/login/?next=/')

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
    ml = {'jl':('剑来',r'https://tieba.baidu.com/f?kw=%BD%A3%C0%B4&fr=ala0&loc=rec'),
    'ddct':('大道朝天',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E9%81%93%E6%9C%9D%E5%A4%A9&fr=search'),
    'xxtx':('侠行天下',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search')}

    for name,lst in xsdict.items():
        lst.sort(key=lambda x:x[0])
        data = ml.get(name)
        if cname:
            last20[(name,data[0],data[1])] = lst[:-6:-1]
        else:
            last20[(name,name,'#')] = lst[:-6:-1]
        



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


def asset_view(request):
    if not get_user_group(request.user,'super'):
        return HttpResponseRedirect('/admin/login/?next=/')
    assets = getres()
    # from pprint import pprint
    # pprint(assets)
    assets = '\n'.join(assets)
    assets += '\n\n' + get_wal_data()
    return render(request,'asset.html',{'assets':assets})


def get_user_group(request,groupname=None):

    try:
        user = request.user
    except Exception:
        user = request
    if user.is_anonymous:
        return None

    if user.is_superuser:
        if not groupname:
            return 'super'
        else:
            mygname = 'super'
    elif not  groupname:
        if user.groups.all():
            return user.groups.all()[0].name
    else:
        if user.groups.all():
            mygname = user.groups.all()[0].name
        else:
            mygname = None
    return mygname == groupname