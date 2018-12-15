# 日历的功能


import re
import datetime
import time
import traceback
try:
    from PyQt5.QtGui import QBrush,QColor
    from gl import myexec
except Exception:
    pass

def main():
    text = '12312sfg gdghtrh <hisory>\n20181209 11:16:56\n20181210 11:16:56\n</history>'
    history = re.findall(r'\<history\>[\w\W]+\</history\>',text)
    # print(type(history[0]))
    print(history)

    time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))

    print(text)
    text = text.replace('<history>','<history>\n%s\n'%time_now_str)
    print(text)


    hc = HCalendar()
    text = hc.addhistory(text)

    print(1111111111,text)

def addtime(date,type_,num):
    if isinstance(date,datetime.datetime):
        print('datetime')
    elif isinstance(date,(float,int)):
        date = datetime.datetime.fromtimestamp(date)
    else:
        raise TypeError('错误的参数 %s %s' % (date,type(date)))

    if type_ in ('days','seconds','microseconds','milliseconds','minutes','hours','weeks'):
        date = date + datetime.timedelta(**{type_:num})
        return date
    elif type_ == 'years' and isinstance(num,int):
        oldyear = date.year
        oldstr = date.strftime('%Y%m%d %H:%M:%S')
        newstr = str(oldyear + num) + oldstr[4:]
        new = datetime.datetime.strptime(newstr, '%Y%m%d %H:%M:%S')
        return new
    elif type_ == 'months' and isinstance(num,int):
        oldyear = date.year
        oldmonth = date.month

        newmonth = oldmonth + num - 0.5
        addyear = 0
        if newmonth > 0:
            addyear = int(newmonth / 12)
            newmonth = int(newmonth % 12 + 0.5)
        if newmonth < 0:
            newmonth = int(newmonth)
            while newmonth <= 0:
                newmonth = newmonth + 12
                addyear -= 1

        oldstr = date.strftime('%Y%m%d %H:%M:%S')
        newstr = '%s%02d' % (oldyear + addyear,newmonth) + oldstr[6:]
        new = datetime.datetime.strptime(newstr, '%Y%m%d %H:%M:%S')
        return new
    else:
        raise TypeError('错误的参数 %s %s %s %s' % (num,type_,type(num),type(type_)))
    return date

def addtime_to_seconds(date,type_,num):
    return time.mktime(addtime(date,type_,num).timetuple())

def show_by_seconds(dd):
    try:
        if dd == 'finished':
            return dd
        if not dd:
            return 0
        fh = ''
        if dd <0:
            dd = -dd
            fh = '-'

        S = dd % 60
        dd = int(dd / 60)

        xx = dd
        M = dd % 60

        dd = int(dd / 60)

        H = dd % 60
        H = dd % 24

        day = int(dd / 24)
        return 'rest %s%s:%02d:%02d:%02d'%(fh,day,H,M,S)
    except Exception as e:
        traceback.print_exc()
        print(dd)
        return 0




class HCalendar(object):
    def __init__(self,tree=None,textedit=None):
        self.te = textedit
        self.tree = tree

    def h_sort_by_tree(self,tree):
        # return myexec(globals(),locals())
        try:
            for item in tree.children():
                if item.text(0) == '<日历>':
                    itemlist = []
                    for citem in tree.children(item):
                        itemlist.append((self.get_rest_seconds(citem.model_data['object']),citem))
                    itemlist.sort(key=lambda x: x[0] if x[0] else 0)
                    for tim,citem in itemlist:
                        if tim < 0:
                            citem.setBackground(0,QBrush(QColor(255,170,255)))
                        elif tim < 3600 * 24:
                            n = int(((3600 * 24 - tim) / (3600 * 24)) * (150-50))
                            citem.setBackground(0,QBrush(QColor(255,50+n,255)))
                        elif tim < 3600 * 24 * 7:
                            n = int(((3600 * 24 * 7 - tim) / (3600 * 24 * 6)) * (225-150))
                            citem.setBackground(0,QBrush(QColor(255,50,150+n)))
                        elif tim < 3600 * 24 * 30:
                            n = int(((3600 * 24 * 30 - tim) / (3600 * 24 * 23)) * (225-150))
                            citem.setBackground(0,QBrush(QColor(150+n,50,150)))
                        elif tim < 3600 * 24 * 365:
                            n = int(((3600 * 24 * 365 - tim) / (3600 * 24 * 335)) * (150-50))
                            citem.setBackground(0,QBrush(QColor(50,150,50+n)))
                        elif tim < 3600 * 24 * 365 * 5:
                            n = int(((3600 * 24 * 365 * 5 - tim) / (3600 * 24 * 365 * 4)) * (150-50))
                            citem.setBackground(0,QBrush(QColor(50+n,50,50)))
                        else:
                            citem.setBackground(0,QBrush(QColor(50,50,50)))



                        # if tim < 0:
                        #     print(11)
                        #     citem.setBackground(0,QBrush(QColor(255,255,255)))
                        # elif tim < 3600 * 24:
                        #     n = int(((3600 * 24 - tim) / (3600 * 24)) * (255-50))
                        #     citem.setBackground(0,QBrush(QColor(50,255-n,50)))
                        # elif tim < 3600 * 24 * 7:
                        #     n = int(((3600 * 24 * 7 - tim) / (3600 * 24 * 6)) * (120-50))
                        #     citem.setBackground(0,QBrush(QColor(50,255,120-n)))
                        # elif tim < 3600 * 24 * 30:
                        #     n = int(((3600 * 24 * 30 - tim) / (3600 * 24 * 23)) * (120-50))
                        #     citem.setBackground(0,QBrush(QColor(120-n,255,120)))
                        # elif tim < 3600 * 24 * 365:
                        #     n = int(((3600 * 24 * 365 - tim) / (3600 * 24 * 335)) * (255-120))
                        #     citem.setBackground(0,QBrush(QColor(120,255,255-n)))
                        # elif tim < 3600 * 24 * 365 * 5:
                        #     n = int(((3600 * 24 * 365 * 5 - tim) / (3600 * 24 * 365 * 4)) * (255-120))
                        #     citem.setBackground(0,QBrush(QColor(255-n,255,255)))
                        # else:
                        #     citem.setBackground(0,QBrush(QColor(255,255,255)))








                        tree.removeItem(citem)
                        tree.addItem(item, citem)
        except Exception as e:
            traceback.print_exc()

    def show_by_seconds(self,obj):
        return show_by_seconds(self.get_rest_seconds(obj))

    def get_rest_seconds(self,obj):
        try:

            di = self.getdict(obj)
            if not di:
                return None
            history = self.gethistory(obj.text)

            lasthistory = 0
            start = di['start']
            interval = di.get('interval')
            end = di.get('end')
            times = di.get('times')


            if history:
                lasthistory = max(history)

            if not interval and not end and not times:
                if lasthistory:
                    return 'finished'
                return start - time.time()

            elif interval:
                end_times = 0
                lasthistory_times = 0
                if end:
                    starttemp = start
                    while True:
                        starttemp = addtime_to_seconds(starttemp,*interval)
                        end_times += 1
                        if starttemp > end:
                            break

                if lasthistory:
                    starttemp = start
                    while True:
                        starttemp = addtime_to_seconds(starttemp,*interval)
                        lasthistory_times += 1
                        if starttemp > lasthistory:
                            break
                if (times and lasthistory_times >= times) or (end_times and lasthistory_times >= end_times):
                    return 'finished'
                else:
                    if not lasthistory_times:
                        lasthistory_times += 1
                    return addtime_to_seconds(start,interval[0],interval[1]*lasthistory_times)- time.time()
            else:
                print(133333,interval)

        except Exception as e:
            traceback.print_exc()

    def getdict(self,obj):
        timedict = re.findall(r'\<time\>([\w\W]+)\</time\>',obj.text)
        if not timedict:
            return None
        timedict = timedict[0].strip()
        timedict = [ s.split('|') for s in timedict.split('\n') if s.strip()]
        if not timedict:
            return None
        timedict = dict(timedict)
        timedict['object'] = obj
        
        return self.dealdict(timedict)

    def dealdict(self,di):
        start = di.get('start')
        if not start:
            start = di['object'].create_date + datetime.timedelta(hours=8)
        else:
            start = datetime.datetime.strptime(start, '%Y%m%d %H:%M:%S')
        di['start'] = time.mktime(start.timetuple())

        end = di.get('end')
        if end:
            end = end.strip()
            end = datetime.datetime.strptime(end, '%Y%m%d %H:%M:%S')
            di['end'] = time.mktime(end.timetuple())

        times = di.get('times')
        if times:
            times = times.strip()
            di['times'] = int(times)

        interval = di.get('interval')
        if interval:
            interval = interval.strip()
            num = re.findall(r'\d+',interval)[0]
            interval = (interval[len(num):],int(num))
            di['interval'] = interval

        return di

    def gethistory(self,text):
        historylst = re.findall(r'\<history\>([\w\W]+)\</history\>',text)
        if not historylst:
            return None
        historylst = historylst[0].strip()
        historylst = re.findall(r'\<(\d{8} \d{2}:\d{2}:\d{2})\>',historylst)
        historylst = [ time.mktime(datetime.datetime.strptime(date, '%Y%m%d %H:%M:%S').timetuple()) for date in historylst]
        return historylst

    def addhistory(self,text):
        history = re.findall(r'\<history\>[\w\W]+\</history\>',text)
        time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
        if history:
            if len(history) != 1:
                print('获得了多个history')
                return text
            text = text.replace('<history>','<history>\n<%s>\n'%time_now_str)
        else:
            text = text +('\n<history>\n<%s>\n</history>\n'%time_now_str)

        return text



if __name__ == '__main__':
    main()