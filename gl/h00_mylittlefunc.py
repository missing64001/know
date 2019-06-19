import struct
import os
import time
import pickle
import sys
import inspect
from functools import reduce
CURRENTURL = os.path.dirname(__file__)





x='''
# 装饰器 指定程序出错运行次数
tryruntime(fun,times=5)

# 获得link的实际地址
get_link(path)

# 装饰器 数据如果存在则判断时间，超时或不存在则重新读取
opt_read(T=5*60,end='\r',pa=None)


# 装饰器 拦截错误
dec_try(errC=None,err=None)
    errC 错误类别
    err 错误内容


'''
__all__ = ['tryruntime', 'get_link', 'opt_read', 'dec_try', ]


def runfilepath(*path):
    x = inspect.stack()[-1]
    return os.path.join(os.path.dirname(x.filename),*path)


# 装饰器 指定程序出错运行次数
def tryruntime(fun,times=5):
    def inner(*args,**kw):
        runtimes = 0
        while True:
            runtimes += 1
            try:
                data = fun(*args,**kw)
                return data
            except Exception as e:
                print('出错 2秒后 重启')
                time.sleep(2)
                if runtimes >= times:
                    raise e
    return inner




# 获得link的实际地址
def get_link(path):
    try:
        with open(path, 'rb') as stream:
            content = stream.read()

            # skip first 20 bytes (HeaderSize and LinkCLSID)
            # read the LinkFlags structure (4 bytes)
            lflags = struct.unpack('I', content[0x14:0x18])[0]
            position = 0x18

            # if the HasLinkTargetIDList bit is set then skip the stored IDList 
            # structure and header
            if (lflags & 0x01) == 1:
                position = struct.unpack('H', content[0x4C:0x4E])[0] + 0x4E

            last_pos = position
            position += 0x04

            # get how long the file information is (LinkInfoSize)
            length = struct.unpack('I', content[last_pos:position])[0]

            # skip 12 bytes (LinkInfoHeaderSize, LinkInfoFlags, and VolumeIDOffset)
            position += 0x0C

            # go to the LocalBasePath position
            lbpos = struct.unpack('I', content[position:position+0x04])[0]
            position = last_pos + lbpos

            # read the string at the given position of the determined length
            size= (length + last_pos) - position - 0x02
            temp = struct.unpack('c' * size, content[position:position+size])
            target = ''.join([chr(ord(a)) for a in temp])
    except:
        # could not read the file
        pass




# 装饰器 数据如果存在则判断时间，超时或不存在则重新读取
def opt_read(T=5*60,end='\r',pa=None):
    def _opt_read(fun):
        def inner(*arg,**kw):
            path = pa
            # abspath = runfilepath('gl')
            abspath = os.path.join(CURRENTURL,'gl','__opt_read')
            if not os.path.exists(abspath):
                os.makedirs(abspath)

            if not path:
                path = fun.__qualname__
            path = os.path.join(abspath,path+'.dat')

            if os.path.exists(path):
                t1 = time.time() - os.path.getmtime(path)
                if t1 < T or T == -1:
                    print('\r'+' '*20+'\r' + '还有%d秒过期'%(T-t1),end=end)
                    filename = path
                    with open(filename,'rb') as f:
                        data = pickle.load(f)
                    return data
            print('重新读取数据',end=end)
            data = fun(*arg,**kw)
            if data:
                filename = path
                with open(filename,'wb') as f:
                    pickle.dump(data,f)
            return data

        return inner
    return _opt_read

def myreduce(fun,lst,deal_data_fun=None):
    # 意义不大相当于 reduce前 做了一下数据处理
    if deal_data_fun:
        lst = [deal_data_fun(l) for l in lst]
    return reduce(fun,lst)


@opt_read(1222,'\r','test.dat')
def xx():
    return 55


# 装饰器 拦截错误
def dec_try(errC=None,err=None):
    if not errC:
        errC = Exception
    def _dec_try(fun):
        def inner(*args,**kw):
            try:
                data = fun(*args,**kw)
                return data
            except errC as e:
                if err and e != err:
                    raise e
                print('拦截了 %s :%s' % (errC,e))
                    
        return inner
    return _dec_try











@dec_try(err='123')
def test(a):
    print(a)




if __name__ == '__main__':
    test()


def test():
    print(111)

    open = tryruntime(open)
    with open('123.txt','r') as f:
        f.read()

    exit()
    a = [1,3,4,5,7]
    b = [3]
    a = myreduce(lambda x,y:str(x)+str(y),a)
    print(a)
    b = myreduce(lambda x,y:str(x)+str(y),b)
    print(type(b))
