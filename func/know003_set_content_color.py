# 设置content的背景颜色
from hmysql import MyModels,Label,Content
import re

from PyQt5.QtGui import QBrush, QColor
def setContentColor(self,models):
    get_contents_by_label = models.get_contents_by_label
    cobj = MyModels(Content,None,170)
    if cobj.name != 'know_setting':
        raise ValueError('name is %s not know_setting' % cobj.name)
    res = re.findall(r'\<color\>([\w\W]+)\<colorend\>',cobj.text)[0].split('\n')
    colorlabels = {int(r.strip().split('|')[0])  : r.strip().split('|')[1] for r in res if r}


    labeldict,contentdict = self.tree.content_and_label_id_items_dict()
    for i,color in colorlabels.items():
        contents = get_contents_by_label.get(i)
        if not contents:
            continue
        for j,item in contentdict.items():
            if j in contents:
                item.setBackground(0,QBrush(QColor("#"+color)))