
import re
import datetime
import time

def main():


    hc = HCalendar(1,2)
    rest = hc.get_rest_seconds(1)
    if rest != 'finished':
        sc = show_by_seconds(rest)
        print(sc)
    else:
        print('finished')
    # print(time.time())

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
        print('错误的参数 %s %s %s %s' % (num,type_,type(num),type(type_)))
    return date

def addtime_to_seconds(date,type_,num):
    return time.mktime(addtime(date,type_,num).timetuple())

def show_by_seconds(dd):
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

class HCalendar(object):
    def __init__(self,tree,textedit):
        self.te = textedit
        self.tree = tree

    def h_sort(self):
        for item in self.tree.children():
            if item.text() == '<日历>':
                citems = self.tree.children(item)

    def show_by_seconds(self,obj):
        return show_by_seconds(self.get_rest_seconds(obj))

    def get_rest_seconds(self,obj):
        # obj = item.model_data['object']
        di = self.getdict(obj)
        if not di:
            return None
        histroy = self.gethistroy(obj)

        # di = {'start':1544140036,'interval':('days',1),'times':5,'end':1544290136 + 3 * 24 * 3600}
        # histroy = {1544100056 + 3 * 24 * 3600}

        # print('now',datetime.datetime.fromtimestamp(time.time()))
        # print('sta',datetime.datetime.fromtimestamp(di['start']))
        # print('end',datetime.datetime.fromtimestamp(di['end']))
        # print('his',datetime.datetime.fromtimestamp(max(histroy)))


        lasthistroy = 0
        start = di['start']
        interval = di.get('interval')
        end = di.get('end')
        times = di.get('times')


        if histroy:
            lasthistroy = max(histroy)

        if not interval and not end and not times:
            if lasthistroy:
                return 'finished'
            return start - time.time()

        elif interval:
            end_times = 0
            lasthistroy_times = 0
            if end:
                starttemp = start
                while True:
                    starttemp = addtime_to_seconds(starttemp,*interval)
                    end_times += 1
                    if starttemp > end:
                        break

            if lasthistroy:
                starttemp = start
                while True:
                    starttemp = addtime_to_seconds(starttemp,*interval)
                    lasthistroy_times += 1
                    if starttemp > lasthistroy:
                        break
            if (times and lasthistroy_times >= times) or (end_times and lasthistroy_times >= end_times):
                return 'finished'
            else:
                return addtime_to_seconds(start,interval[0],interval[1]*lasthistroy_times)- time.time()
        else:
            print(133333,interval)


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

    def gethistroy(self,obj):
        histroylst = re.findall(r'\<histroy\>([\w\W]+)\</histroy\>',obj.text)
        if not histroylst:
            return None
        histroylst = histroylst[0].strip()
        histroylst = re.findall(r'\<(\d{8} \d{2}:\d{2}:\d{2})\>',histroylst)
        histroylst = [ time.mktime(datetime.datetime.strptime(date, '%Y%m%d %H:%M:%S').timetuple()) for date in histroylst]
        return histroylst

if __name__ == '__main__':
    main()