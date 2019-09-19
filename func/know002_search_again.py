# 重新搜索 当前label即content 数据
# 需要进一步优化 搜索后显示单独的content


import copy


def know002_search_again(self,txt):
    txt = txt.lower()
    from PyQt5.QtGui import QFont, QColor, QBrush
    citems = self.tree.children()
    citemall = citems
    while citems:
        citems_old = citems
        citems = []
        for citem in citems_old:
            citems += self.tree.children(citem)
        for citem in citems:
            if citem not in citemall:
                citemall.append(citem)
    
    text = self.le1.text()
    print(txt)
    all_change_citem = []
    for citem in citemall:
        mym = citem.model_data['object']
        if str(mym.model) == "<class 'data.models.Label'>":
            if txt in mym.name.lower():
                citem.setForeground(0,QBrush(QColor("#aa3333")))
                continue
        else:
            if txt in mym.name.lower():
                citem.setForeground(0,QBrush(QColor("#aa3333")))
                all_change_citem.append(citem.model_data['object'].id)
                continue
            elif txt in mym.text.lower():
                citem.setForeground(0,QBrush(QColor("#557033")))
                all_change_citem.append(citem.model_data['object'].id)
                continue
        citem.setForeground(0,QBrush(QColor("#000000")))

    # 原有label上的重新搜索再优化 1829
    self.tree.set_content_to_tree_top(all_change_citem)




    # print(len(citemall))