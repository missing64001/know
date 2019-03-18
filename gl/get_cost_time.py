

_='''
通过装饰器计算程序的运行时间
gctdec:计算时间的装饰器 tprintex():计算时间 并且输出每个程序的 运行总时间 运行次数 单个运行时间
gcts 单独计算时间 类似print 第二个参数


gctdec = importitems[2].gctdec
tprintex = importitems[2].tprintex
gcts = importitems[2].gcts


'''

import time
from pprint import pprint
import sys

def main():
    

    gcts(22)
    run()
    gcts(11)
    di = {1:3,5:6,3:'33dldj给零点十分感激受到攻击时 离开国家队两个积分电视里看过离开过历史告诉老公胜利开工是独立开关',
    55:142343546576675764564}
    gcts(di,issm=True)
    # gCtime.print()

class CostTimeSingle(object):
    def __init__(self):
        self.lasttime = None

    def getctS(self,s='',issm=False,isprint=True):
        'issm is show __module__'
        t = None
        if self.lasttime:
            t = time.time() - self.lasttime

            mname = 'h'
            if issm:
                mname = sys._getframe().f_back.f_globals['__name__']
            if isprint:
                print('%8.2f--%s:%s  %s'%(t,mname,sys._getframe().f_back.f_lineno,s))
        self.lasttime = time.time()
        return t


        

class GetCostTimeLog(object):
    """docstring for GetCostTimeLog"""
    def __init__(self):
        self.timedict = {}

    def print(self):
        for key,val in sorted(self.timedict.items(),key=lambda x:x[1][0],reverse=True):
            print(      '%10.3f  %s %s'  % (val[0],key,val[1]))

    def printex(self):
        pprint (self.timedict)



gcts = CostTimeSingle()
gcts = gcts.getctS

gCtime = GetCostTimeLog()

tprint = gCtime.print
tprintex = gCtime.printex





def gctdec(fun):
    def inner(*args,**kw):
        fun_name = '%s:%s'%(fun.__module__,fun.__qualname__)
        stime = time.time()
        res = fun(*args,**kw)
        etime = time.time()
        thetime = etime - stime

        gct = gCtime.timedict.get(fun_name)
        if not gct:
            gct = [0,0,[]]
            gCtime.timedict[fun_name] = gct

        gct[0] = gct[0] + thetime
        gct[1] += 1
        gct[2].append(thetime)
        # print(fun_name,gct)
        return res
    return inner

# @gctdec
def run():
    print('run main b')
    time.sleep(1)
    print('run main e')
        
if __name__ == '__main__':
    main()