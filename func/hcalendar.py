
import re
from datetime import datetime
import time

def main():


    datetime.strptime(start, '%Y%m%d %H:%M:%S')
    x = (d2-d1).seconds
    print(x)

    start = di['object'].create_date + datetime.timedelta(hours=8)
    start = datetime.strptime(start, '%Y%m%d %H:%M:%S')

class HCalendar(object):
    """docstring for Calendar"""
    def __init__(self,tree,textedit):
        self.te = textedit
        self.tree = tree

    def h_sort(self):
        for item in self.tree.children():
            if item.text() == '<日历>':
                citems = self.tree.children(item)

    def get_rest_seconds(self,item):
        obj = item.model_data['object']
        di = self.getdict(obj)
        histroy = self.gethistroy(obj)
        lasthistroy = None
        start = di['start']
        interval = di.get('interval')
        end = di.get('end')
        times = di.get('times')


        if histroy:
            lasthistroy = max(histroy)

        if not interval and not end and not times:
            if lasthistroy:
                return 'finished'
            return time.time() - start

        elif 'interval' in di:
            pass



        
    def getdict(self,obj):
        timedict = re.findall(r'\<time\>([\w\W]+)\</time\>',obj.text)[0].strip()
        timedict = [ s.split(':') for s in timedict.split('\n') if s.strip()]
        timedict = dict(res2)
        timedict['object'] = obj
        return self.dealdict(timedict)

    def dealdict(self,di):
        start = di.get('start')
        if not start:
            start = di['object'].create_date + datetime.timedelta(hours=8)
        else:
            start = datetime.strptime(start, '%Y%m%d %H:%M:%S')
        di['start'] = time.mktime(start.timetuple())

        end = di.get('end')
        if end:
            end = end.strip()
            end = datetime.strptime(end, '%Y%m%d %H:%M:%S')
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

        # workday
        # before

    def gethistroy(self,obj):
        histroylst = re.findall(r'\<histroy\>([\w\W]+)\</histroy\>',obj.text)[0].strip()
        histroylst = re.findall(r'\<(\d{8} \d{2}:\d{2}:\d{2})\>',histroylst)
        histroylst = [ time.mktime(datetime.strptime(date, '%Y%m%d %H:%M:%S').timetuple()) for date in histroylst]
        return histroylst

if __name__ == '__main__':
    main()