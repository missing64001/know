


def gethistory(text):
    historylst = re.findall(r'\<history\>([\w\W]+)\</history\>',text)
    print(historylst)
    if not historylst:
        return None
    historylst = historylst[0].strip()

    print(111,historylst)
    historylst = re.findall(r'\<(\d{8} \d{2}:\d{2}:\d{2})\>',historylst)

    print(222,historylst)

    historylst = [ time.mktime(datetime.datetime.strptime(date, '%Y%m%d %H:%M:%S').timetuple()) for date in historylst]
    return historylst











global RES

try:    
    di = self.getdict(obj)
    if not di:
        RES = None #return None
    history = gethistory(obj.text)

    lasthistory = 0
    start = di['start']
    interval = di.get('interval')
    end = di.get('end')
    times = di.get('times')

    print(history)
    if history:
        lasthistory = max(history)

    if not interval and not end and not times:
        if lasthistory:
            RES = 'finished' # return 'finished'
        RES = start - time.time() #return start - time.time()

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
            RES = 'finished' # return 'finished'
        else:
            print(11,lasthistory_times)
            if not lasthistory_times:
                lasthistory_times += 1
            RES = addtime_to_seconds(start,interval[0],interval[1]*lasthistory_times)- time.time() #return addtime_to_seconds(start,interval[0],interval[1]*lasthistory_times)- time.time()
    else:
        print(133333,interval)

except Exception as e:
    traceback.print_exc()

print(RES)