import sys
import os
CURRENTURL = os.path.dirname(__file__)

paths = [r'F:\my',]
for path in paths:
    if os.path.exists(path):
        sys.path.insert(1,path)
        break
else:
    print('not find my model in ',paths)

from F00_myfn.h11_myexec import myexec
from F00_myfn.h09_get_bios import get_computer_info