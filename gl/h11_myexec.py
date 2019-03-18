
import inspect
from pprint import pprint
import sys
import re
import traceback
import os
CURRENTURL = os.path.dirname(__file__)

TEST = False

def main():

    aa = xx()
    print(aa.a())

    aa.b()

    input('11')
    print(aa.a())







    # while True:
    #     print(xxx())


# def myexec11(fun,aaa,**bc):
#     def inner():

#         s1 = inspect.stack()[1].code_context[0]
#         s2 = inspect.getsource(sys._getframe().f_back)
#         s3 = s2.split(s1)[1]

#         skong = re.findall(r'(^\W*)',s1)
#         skong = skong[0]
#         lenth = len(skong)

#         s3 = '\n'.join([ s[lenth:] for s in s3.split('\n')])
#         # print(s3)


#         rs = re.findall(r'\n\W*return.*',s3)
#         rs = set(rs)

#         # print(rs)
#         for r in rs:
#             skong = re.findall(r'(^\W*)',r)
#             skong = skong[0]
#             lenth = len(skong) - 1
#             # print(lenth)

#             res = r.replace('return','RES[0] = ') + '%sraise TypeError("no bug")' % skong
#             s3 = s3.replace(r,res)

#         # print(s3)
        

#         s3 = 'global RES\n' + s3
#         # s3 = 'global RES\nRES=3'
#         print(s3)
#         try:
#             fun(s3,bc)
#         except TypeError as e:
#             if str(e) == 'no bug':
#                 pass
#             else:
#                 raise e
#         print(RES)
#         return RES[0]
#     return inner

def dectry(fun):
    def inner(*args,**kw):
        try:
            return fun(*args,**kw)
        except Exception:
            traceback.print_exc()
    return inner





# @dectry
def myexec(di=True):
    try:
        s3 = None
        bc = {}
        gl = sys._getframe().f_back.f_globals
        lc = sys._getframe().f_back.f_locals

        if gl:
            bc.update(gl)
        if lc:
            bc.update(lc)

        s1 = inspect.stack()[1].code_context[0]
        s2 = inspect.getsource(sys._getframe().f_back)
        s3 = s2.split(s1)[1]

        skong = re.findall(r'(^\W*)',s1)
        skong = skong[0]
        lenth = len(skong)

        s3 = '\n'.join([ s[lenth:] for s in s3.split('\n')])
        # print(s3)


        rs = re.findall(r'\n\W*return.*',s3)
        rs = set(rs) | set(re.findall(r'^\W*return.*',s3))

        # print(rs)
        for r in rs:
            skong = re.findall(r'(^\W*)',r)
            skong = skong[0]
            lenth = len(skong) - 1
            # print(lenth)
            if not skong:
                skong = '\n'
            res = r.replace('return','RES = ') + '%sreslst_reslst.append(RES)%sraise TypeError("no bug")' % (skong,skong)
            s3 = s3.replace(r,res)

        # print(s3)
        

        # s3 = 'global RES\nRES = None\n' + s3
        # s3 = 'global RES\nRES=3'
        # print(s3)
        # filename = 'test.py'
        # with open(filename,'w',encoding='utf-8') as f:
        #     f.write(s3)



        reslst_reslst = []
        bc.update({'reslst_reslst':reslst_reslst})
        try:
            exec(s3,bc)
        except TypeError as e:
            if str(e) == 'no bug':
                pass
            else:
                filename = os.path.join(CURRENTURL,'h11_myexec.txt')
                with open(filename,'w',encoding='utf-8') as f:
                    f.write(s3)
                traceback.print_exc()
        except Exception:
            filename = os.path.join(CURRENTURL,'h11_myexec.txt')
            with open(filename,'w',encoding='utf-8') as f:
                f.write(s3)
            traceback.print_exc()
        finally:
            filename = os.path.join(CURRENTURL,'h11_myexec.txt')
            with open(filename,'w',encoding='utf-8') as f:
                f.write(s3)

        # print(reslst_reslst)
        if reslst_reslst:
            return reslst_reslst[-1]
        return None
    except Exception:
        print('----------s1----------')
        pprint(s1)
        print('----------s2----------')
        pprint(s2)
        print('----------s3----------')
        pprint(s3)
        traceback.print_exc()




def dec(fun):
    def inner(*arg,**kw):
        print('run dec')
        return fun(*arg,**kw)
    return inner


def xxx():
    return myexec(globals(),locals())



    # print('cc')
    x = input('请输入')
    # print(x)
    # print(bb)
    if x == 'a':
        return '11'
    elif x == '2':
        return '22'
    elif x == '5':
        return '55333332222111111122233'
    return '35'



class xx(object):

    @dec
    def a(self):
        return myexec()

        return 444444655556

    @dec
    def b(self):
        print('b')
        
if __name__ == '__main__':
    main()
