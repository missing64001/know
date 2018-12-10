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