# 词霸天下优化操作

import pyperclip
import re

def trans():
    data = pyperclip.paste()

    data = data.split('\n')


    reslst = []
    for da in data:
        rrr = re.findall(r" (\[[\w\W]+?\]) ",da)
        if rrr:
            rrr = rrr[0]
            da = da.replace(' %s ' % rrr,'\n    %s\n    ' %rrr)
        reslst.append(da)

    res = '\n\n'.join(reslst) + '\n\n'
    pyperclip.copy(res)