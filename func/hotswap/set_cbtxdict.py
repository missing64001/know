# # 设置词霸天下的字典 以便ctrl+左键使用

# LABEL_FIELDS = ('id','name','pid','queue','grade','create_date')
# CONTENT_FIELDS = ('id','name','text','create_date')
# self.labeldict = None
# self.contentdict = None
# self.get_labels_by_content = None
# self.get_contents_by_label = None
import re
def setCBTXDict():
    self.textEdit.cbtxdict = dict()
    pid = 468
    allpid = set()
    allcontents = set()
    for i,data in self.models.labeldict.items():
        if data[2] == pid:
            allpid.add(i)
    for labelid in allpid:
        contents = self.models.get_contents_by_label.get(labelid,set())
        allcontents |= contents
    for i,contentid in enumerate(list(allcontents)):  # [2:] 为什么要加这个？
        data = self.models.contentdict[contentid][2]
        data = data.strip().split('\n')
        for da in data:
            if not da:
                pass
            elif da[0] == ' ':
                self.textEdit.cbtxdict[title] = self.textEdit.cbtxdict.get(title,'') + da + '\n'
            else:
                title = da.strip()
    print('词霸天下 单词设置完成' , end ='\r')

# setCBTXDict()


# xx = '''
# vanity
#     n.  虚荣心；空虚；浮华；无价值的东西【词频9704】 
#     空 -> 空虚 -> 虚荣 + ity 
# vanish
#     vi.  消失；突然不见；成为零  vt.  使不见，使消失  
#     n.  弱化音【词频3980】【X6M2】 
#     空 -> 没 小时 +ish 动名词后缀
# vanishing
#     adj.  消没的  n.  消失【词频14656】 

# vanishingly
#     adv.  难以察觉地；消遁似地；趋于零地【词频39132】 

# evanish
#     vi.  消失；消灭 

# evanesce
#     vi.  消散；逐渐看不见 
#     e- 向外 + 空 -> 消失

# evanescence
#     n.  逐渐消失；瞬息；幻灭【词频45313】 

# evanescent
#     adj.  容易消散的；逐渐消失的；会凋零的【词频28766】

# '''

# from pprint import pprint
# cbtxdict = dict()
# data = xx.strip().split('\n')
# for da in data:
#     if not da:
#         pass
#     elif da[0] == ' ':
#         cbtxdict[title] = cbtxdict.get(title,'') + da + '\n'
#     else:
#         title = da.strip()

# pprint(cbtxdict)