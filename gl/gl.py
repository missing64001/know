import sys
import os
CURRENTURL = os.path.dirname(os.path.dirname(__file__))


basepath = r'F:\my'

imports = [
            ('F00_myfn','h11_myexec'),
            ('F00_myfn','h09_get_bios'),
            ('F00_pythonself','get_cost_time'),
            ('F00_myfn','h00_mylittlefunc'),
            ]

localpath = os.path.join(CURRENTURL,'gl')
if not os.path.exists(localpath):
    os.makedirs(localpath)


importitems = []

import time


for im in imports:
    path = os.path.join(basepath,*im[:-1],im[-1]+'.py')
    localfile = os.path.join(localpath,im[-1]+'.py')
    if os.path.exists(path):
        filename = path
        with open(filename,'rb') as f:
            data = f.read()

        filename = localfile
        with open(filename,'wb') as f:
            f.write(data)


    x = __import__('gl.%s'%im[-1])
    importitems.append(getattr(x,im[-1]))


myexec = importitems[0].myexec
get_computer_info = importitems[1].get_computer_info
gctdec = importitems[2].gctdec
tprintex = importitems[2].tprintex
gcts = importitems[2].gcts

tryruntime = importitems[3].tryruntime
open = tryruntime(open)

# setattr(M,'myexec',importitems[0].myexec)
# setattr(M,'get_computer_info',importitems[1].get_computer_info)

# print(M)




# exit()


# paths = [r'F:\my']
# for path in paths:
#     if os.path.exists(path):
#         sys.path.insert(1,path)
#         break
# else:
#     print('not find my model in ',paths)

# from F00_myfn.h11_myexec import myexec
# from F00_myfn.h09_get_bios import get_computer_info