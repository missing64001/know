
import os
import time
import math

CURRENTURL = os.path.dirname(__file__)
FILENAME = os.path.join(CURRENTURL,'labelhistory.txt')

class LabelHistory(object):
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self):
        self.historyList = None
        self.readFile()

    def readFile(self):
        filename = FILENAME
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as f:
                data = f.read()
                data = data.split('\n')
                data = [[ da.split(',')[0],float(da.split(',')[1])] for da in data if da]

            self.historyList = data
        else:
            self.historyList = []

    def addHistory(self,str_):
        dt = time.time()

        filename = FILENAME
        with open(filename,'a',encoding='utf-8') as f:
            f.write('%s,%s\n' % (str_,dt))
        self.historyList.append([str_,dt])

    def getSort(self):
        now = time.time()
        historyDict = {}
        for name,t in self.historyList:
            historyDict[name] = historyDict.get(name,0) + 0.5 ** (now-t)
        lst = list(historyDict.items())
        lst.sort(key=lambda x: x[1])
        return [l[0] for l in lst[::-1]]

def main():
    lh = LabelHistory()
    lh.addHistory('gfsd')
    print(lh.getSort())

if __name__ == '__main__':
    main()