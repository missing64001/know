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
import time
import datetime
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
        time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
        cobj.text = cobj.text + '\n%s\n%s' % (time_now_str,txt)
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
                date = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(curdir,file)))
                if lst:
                    lst.append((int(res[1]),res[1] + ' ' + res[2],os.path.join(curdir,file),date))
                else:
                    xsdict[res[0]] = [(int(res[1]),res[1] + ' ' + res[2],os.path.join(curdir,file),date)]


        break

    # pprint(xsdict)
    last20 = {}
    ml = {
    # 'jl':('剑来',r'https://tieba.baidu.com/f?kw=%BD%A3%C0%B4&fr=ala0&loc=rec'),
    'ddct':('大道朝天',r'http://120.79.41.9:8888/getxsdata?name=ddct'),
    'xxtx':('侠行天下',r'http://120.79.41.9:8888/getxsdata?name=xxtx'),
    'gmzz':('诡秘之主',r'http://120.79.41.9:8888/getxsdata?name=gmzz'),
    # 'cjzj':('重生之超级战舰',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search'),
    # 'dqjy':('地球纪元',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search'),
    }

    for name,lst in xsdict.items():
        lst.sort(key=lambda x:x[0])
        data = ml.get(name)
        if data:
            last20[(name,data[0],data[1])] = lst[:-6:-1]
        # else:
        #     last20[(name,name,'#')] = lst[:-6:-1]
        



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

    name = request.GET.get('name')
    if name in ('ddct','xxtx','gmzz'):
        return get_xs_all_lst(request,name)

    name = name.split('-')
    names = []
    if len(name) == 3:
        for i in range(int(name[2])):
            names.append(name[0] + str(int(name[1])+i))
    else:
        names.append(request.GET.get('name'))

    data = ''
    for name in names:
        filename = xsdict[name]
        with open(filename,'r') as f:
            data += f.read() + '\n'
    data = '<br/>'.join([da.strip() for da in data.split('\n') if da.strip()])
    return HttpResponse(data)
    return render(request,'xsdata.html',{'data':data})

def get_xs_all_lst(request,abname):

    directory = os.path.dirname(os.path.dirname(CURRENTURL))
    directory = os.path.join(directory,'func','xiaoshuo','day')

    xsdict = {}
    for curdir,subdirs,files in os.walk(directory):
        for file in files:
            res = re.findall(r'\d+ (.+?)(\d+) (.+?).txt',file)
            if res:
                res = res[0]
                lst = xsdict.get(res[0])
                date = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(curdir,file)))
                if lst:
                    lst.append((int(res[1]),res[1] + ' ' + res[2],os.path.join(curdir,file),date))
                else:
                    xsdict[res[0]] = [(int(res[1]),res[1] + ' ' + res[2],os.path.join(curdir,file),date)]

        break

    # pprint(xsdict)
    last20 = {}
    ml = {
    # 'jl':('剑来',r'https://tieba.baidu.com/f?kw=%BD%A3%C0%B4&fr=ala0&loc=rec'),
    'ddct':('大道朝天',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A7%E9%81%93%E6%9C%9D%E5%A4%A9&fr=search'),
    'xxtx':('侠行天下',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search'),
    'gmzz':('诡秘之主',r'https://tieba.baidu.com/p/5789305185?red_tag=0917054129'),
    # 'cjzj':('重生之超级战舰',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search'),
    # 'dqjy':('地球纪元',r'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%BE%A0%E8%A1%8C%E5%A4%A9%E4%B8%8B&fr=search'),
    }

    for name,lst in xsdict.items():
        if name != abname:
            continue
        lst.sort(key=lambda x:x[0])
        data = ml.get(name)
        if data:
            last20[(name,data[0],data[1])] = lst[::-1]
        



    return render(request,'xiaoshuo.html',{'xss':last20.items()})



def asset_view(request):
    if not get_user_group(request.user,'super'):
        return HttpResponseRedirect('/admin/login/?next=/')
    assets = getres()
    # from pprint import pprint
    # pprint(assets)
    assets = '\n'.join(assets)
    # assets += '\n\n' + get_wal_data()
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