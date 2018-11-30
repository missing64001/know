import sys
import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame,QSplitter, QStyleFactory, QApplication
from PyQt5.QtWidgets import QTreeWidget, QTextEdit, QMainWindow, QTreeWidgetItem, QLineEdit,QPushButton, QLabel
from PyQt5.QtWidgets import QDialog, QShortcut, QAbstractItemView, QAction ,QMessageBox
from PyQt5.QtCore import Qt, QTimer 
from PyQt5.QtGui import QKeySequence, QIcon, QBrush, QColor, QFont
from pprint import pprint
import sip
from hmysql import models,Q,timezone
import time
from django.db import connection
from functools import reduce
import re
import traceback
import pyperclip
import datetime

CURRENTURL = os.path.dirname(__file__)
paths = [r'F:\my',]
for path in paths:
    if os.path.exists(path):
        sys.path.insert(1,path)
        break
else:
    print('not find my model in ',paths)

from F00_myfn.h09_get_bios import get_computer_info

bios = get_computer_info
if bios[0] == 0:
    file_exe = r'start /b F:\sublime\SublimeText_XP85\sublime_text.exe'
elif bios[0] == 1:
    file_exe = r'"C:\Program Files\Sublime Text 3\sublime_text.exe"'

# from main import models



GTIMES = time.time()



class TextEdit(QTextEdit):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)

    def mouseDoubleClickEvent(self, event):
        try:
            x = self.textCursor()
            self.moveCursor(x.StartOfLine,x.MoveAnchor)
            self.moveCursor(x.EndOfLine,x.KeepAnchor)
            zzz = self.textCursor().selectedText()


            res = zzz.split('|')
            if len(res) == 2:
                if res[0] == 'file':
                    file_name = res[1]
                    os.startfile(file_name)

                elif res[0] == 'sublime':

                    file_name = res[1]
                    # print('start /b '+ file_exe + " " + file_name)
                    os.system(file_exe + " " + file_name) #'start /b '+ 

                elif res[0] == 'python':

                    exeFile = "C:\\Windows\\System32\\cmd"
                    old_path = r'F:\my\P028_knowledge_system\knowqt'
                    # exeFile = 'F:\\my\\P028_knowledge_system\\knowqt\\main.py'
                    exePath = "F:\\my\\P028_knowledge_system\\knowqt\\"

                    file_name = res[1]
                    os.chdir(os.path.dirname(file_name))
                    os.startfile(res[1])
                    # os.system('start /b '+ exeFile)
                    os.chdir(old_path)

                    if len(res)>2:
                        pyperclip.copy(res[2])
                        print(res[2][:-1])
                    if len(res)>3 and res[3]=='g':
                        pyperclip.copy(res[2]+'\r\n')
                        print(3)


                elif res[0] == 'django':


                    exeFile = "C:\\Windows\\System32\\cmd.exe"
                    exeFile = 'F:\\my\\P028_knowledge_system\\knowqt\\main.py'
                    exePath = "F:\\my\\P028_knowledge_system\\knowqt\\"
                    # os.chdir(exePath)
                    # os.startfile(exeFile)
                    # help(os.startfile)
                    file_name = res[1]



                    filename = r'F:\my\P028_knowledge_system\knowqt\myfn\h10_try_command_file.txt'
                    with open(filename,'w',encoding='utf-8') as f:
                        f.write(file_name)
                    os.chdir(os.path.dirname(file_name))
                    os.startfile(r'F:\my\P028_knowledge_system\knowqt\myfn\h10_try_command.py')






                    # file_name = res[1]
                    # file_name = "C:\\Windows\\System32\\cmd"

                    # filename = 'F:\\my\\F00_myfn\\h10_try_command_file.txt'
                    # with open(filename,'w',encoding='utf-8') as f:
                    #     f.write(file_name)
                    # os.chdir(os.path.dirname(file_name))
                    # os.startfile('F:\\my\\F00_myfn\\h10_try_command.py')




        except:
            traceback.print_exc()
        super().mouseDoubleClickEvent(event)

    def exec_test(self):
        print('run_exec_test')

        old_path = r'F:\my\P028_knowledge_system\knowqt'
        os.chdir(old_path)


        filename = 'myexec.py'
        with open(filename,'r',encoding='utf-8') as f:
            data = f.read()
        try:
            exec(data)
        except Exception:
            traceback.print_exc()

class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.setFlags(self.flags() | Qt.ItemIsEditable | Qt.ItemIsEnabled)



class MyTree(QTreeWidget):
    def __init__(self):
        super().__init__()
        # self.setColumnCount(1)
        self.setColumnCount(2)
        self.setColumnWidth(0,200)
        self.setColumnWidth(1,30)



        self.setHeaderHidden(True)
        # self.setitem()
        self.clicked.connect(self.mytree_item_clicked)
        self.itemDoubleClicked.connect(self.itemDoubleClicked_connect)
        self.label_item_dict = {}
        self.content_item_dict = {}


    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Insert):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                # self.close()
                pass
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.add_child_tem()
            else:
                pass

    def set_mself(self,mself):
        self.mself = mself

    def add_child_tem(self):
        mself = self.mself

        mself.show_labels_pre()
        item = self.currentItem()
        if not isinstance(item.model_data['object'], models.Label):
            return

        nitem = TreeWidgetItem(item)
        label = item.model_data['object']


        mself.cl_bt_le.setText('new')
        mself.textEdit.setText('new')
        name = mself.cl_bt_le.text()
        text = mself.textEdit.toPlainText()

        cobj = models.Content.objects.create(name=name,text=text)
        cobj.labels.add(label)

        mself.content_layout_current_id = cobj.id
        mself.show_labels()

        nitem.setText(0,cobj.name)
        nitem.model_data = {
                            'id':cobj.id,
                            'name':cobj.name,
                            'text':cobj.text,
                            'object':cobj,

        }
        nitem.typelc = 'c'
        l = self.content_item_dict.get(cobj.id)
        if l == None:
            self.content_item_dict[cobj.id] = []
            l = self.content_item_dict.get(cobj.id)
        l.append(nitem)

        font = QFont()
        font.setBold(True)
        nitem.setFont(0,font)

        self.setCurrentItem(nitem)




    def setitem_old(self,cobjs=None):
        for i in range(self.topLevelItemCount()):
            sip.delete(self.topLevelItem(0))

        if cobjs == None:
            cobjs = list(models.Content.objects.all())
        else:
            cobjs = list(cobjs)

        for cobj in cobjs:
            item = TreeWidgetItem(self)
            item.setText(0,cobj.name)
            item.model_data = {
                                'id':cobj.id,
                                'name':cobj.name,
                                'text':cobj.text,
                                'object':cobj,
            }

        l = self.content_item_dict.get(cobj.id)
        if l == None:
            self.content_item_dict[cobj.id] = []
            l = self.content_item_dict.get(cobj.id)
        l.append(item)




    def mytree_item_clicked(self):
        item = self.currentItem()
        if item.typelc == 'c':
            self.mysender(item.model_data['id'])

    def set_mysender(self,mysender):
        self.mysender = mysender



    def set_label_treeitems(self,label_id_set,Mself):

        for i in range(self.topLevelItemCount()):
            sip.delete(self.topLevelItem(0))

        labels = [Mself.labeldict[i] for i in label_id_set]
        labels_values = [{
                            'id':Mself.labeldict[i].id,
                            'name':Mself.labeldict[i].name,
                            'pid':Mself.labeldict[i].pid,
                            'queue':Mself.labeldict[i].queue,
                            'grade':Mself.labeldict[i].grade,
                            'create_date':Mself.labeldict[i].create_date,
                        } 
                        for i in label_id_set]

        queue_queue = {'data':None,'children':{}}
        queue_child_dict = {1:queue_queue['children']}
        rest = {}
        for i in range(len(labels)):
            la = labels[i]
            labels_values[i]['object'] = la




            id = labels_values[i]['id']
            name = labels_values[i]['name']
            pid = labels_values[i]['pid']
            queue = labels_values[i]['queue']
            grade = labels_values[i]['grade']
            create_date = labels_values[i]['create_date']

            if pid == -1:
                queue_queue['data'] = labels_values[i]
            elif pid == 1:
                queue_queue['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_queue['children'][id]['children']
            elif pid in queue_child_dict:
                queue_child_dict[pid][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_child_dict[pid][id]['children']
            elif pid in rest:
                rest[pid]['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = rest[pid]['children'][id]['children']
            else:
                rest[id] = {'data':labels_values[i],'children':{}}


        while rest:
            for re in rest.copy():
                id = rest[re]['data']['id']
                name = rest[re]['data']['name']
                pid = rest[re]['data']['pid']
                queue = rest[re]['data']['queue']
                grade = rest[re]['data']['grade']
                create_date = rest[re]['data']['create_date']

                if pid in queue_child_dict:
                    rest_re = rest.pop(re)
                    queue_child_dict[pid][id] = rest_re
                    queue_child_dict[id] = queue_child_dict[pid][id]['children']
                    
                elif pid in rest:
                    rest_re = rest.pop(re)
                    rest[pid]['children'][id] = rest_re
                    queue_child_dict[id] = rest[pid]['children'][id]['children']

                else:

                    rest_re = rest.pop(re)
                    queue_queue['children'][id] = rest_re
                    queue_child_dict[id] = rest_re['children']
        # pprint(queue_queue)

        def add_tree_child_item(pitme,children):
            for child in children['children'].values():
                item = TreeWidgetItem(pitme)
                # print(child['data'])
                item.setText(0,child['data']['name'])
                item.model_data = child['data']
                add_tree_child_item(item,child)

                item.setBackground(0,QBrush(QColor("#CEC1C4")))
                item.typelc = 'l'
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                cobj = item.model_data['object']
                l = self.label_item_dict.get(cobj.id)
                if l == None:
                    self.label_item_dict[cobj.id] = []
                    l = self.label_item_dict.get(cobj.id)
                l.append(item)

        for fchild in queue_queue['children'].values():
            item = TreeWidgetItem(self)

            item.setText(0,fchild['data']['name'])

            # 1 字典 2 model
            item.model_data = fchild['data']
            add_tree_child_item(item,fchild)

            item.setBackground(0,QBrush(QColor("#CEC1C4")))
            item.typelc = 'l'
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

            cobj = item.model_data['object']
            l = self.label_item_dict.get(cobj.id)
            if l == None:
                self.label_item_dict[cobj.id] = []
                l = self.label_item_dict.get(cobj.id)
            l.append(item)


    def setcontent(self,labels,contents,Mself):

        def get_labels_by_content_id_set(content_id_set):
            label_id_set = set()
            for id_ in content_id_set:
                label_id_set.add(Mself.get_labels_by_content.get(id_))
            return label_id_set
            
        def get_contents_by_label_id_set(label_id_set):
            content_id_set = set()
            for id_ in label_id_set:
                content_id_set.add(Mself.get_contents_by_label.get(id_))
            return content_id_set

        def set_content_to_tree(pitem,content_id_set):
            if not content_id_set:
                return 0

            for id_ in content_id_set:
                cobj = Mself.contentdict[id_]
                item = TreeWidgetItem(pitem)
                item.setText(0,cobj.name)
                item.model_data = {
                                    'id':cobj.id,
                                    'name':cobj.name,
                                    'text':cobj.text,
                                    'object':cobj,
                }
                item.typelc = 'c'

                l = self.content_item_dict.get(cobj.id)
                if l == None:
                    self.content_item_dict[cobj.id] = []
                    l = self.content_item_dict.get(cobj.id)
                l.append(item)

                isinname = True
                if self == pitem:
                    textlst = Mself.le1.text().split(' ')
                    
                    for te in textlst:
                        if not te in cobj.name:
                            isinname = False
                            break

                if isinname:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(0,font)

        def set_children_label(pitem):
            total = 0
            for j in range(pitem.childCount()):
                item = pitem.child(j)
                set_children_label(item)

                content_id_set = Mself.get_contents_by_label.get(item.model_data['id'])
                set_content_to_tree(item,content_id_set)




        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            # if item.typelc == 'c':
            #     break
            set_children_label(item)
            content_id_set = Mself.get_contents_by_label.get(item.model_data['id'])
            set_content_to_tree(item,content_id_set)

        set_content_to_tree(self,contents)





    # no use
    def setitem(self,labels=None,contents=None):

        for i in range(self.topLevelItemCount()):
            sip.delete(self.topLevelItem(0))


        if not labels and not contents:
            labels = models.Label.objects.all().order_by('id')
            labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))
        elif not labels:
            labels = []
        else:
            labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))

        # print(len(labels))
        
        labels = list(labels)
        queue_queue = {'data':None,'children':{}}
        queue_child_dict = {1:queue_queue['children']}
        rest = {}

        
        c = 0
        for i in range(len(labels)):
            la = labels[i]
            labels_values[i]['object'] = la




            id = labels_values[i]['id']
            name = labels_values[i]['name']
            pid = labels_values[i]['pid']
            queue = labels_values[i]['queue']
            grade = labels_values[i]['grade']
            create_date = labels_values[i]['create_date']

            if pid == -1:
                queue_queue['data'] = labels_values[i]
            elif pid == 1:
                queue_queue['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_queue['children'][id]['children']
            elif pid in queue_child_dict:
                queue_child_dict[pid][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_child_dict[pid][id]['children']
            elif pid in rest:
                rest[pid]['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = rest[pid]['children'][id]['children']
            else:
                rest[id] = {'data':labels_values[i],'children':{}}


        while rest:
            for re in rest.copy():
                id = rest[re]['data']['id']
                name = rest[re]['data']['name']
                pid = rest[re]['data']['pid']
                queue = rest[re]['data']['queue']
                grade = rest[re]['data']['grade']
                create_date = rest[re]['data']['create_date']

                if pid in queue_child_dict:
                    rest_re = rest.pop(re)
                    queue_child_dict[pid][id] = rest_re
                    queue_child_dict[id] = queue_child_dict[pid][id]['children']
                    
                elif pid in rest:
                    rest_re = rest.pop(re)
                    rest[pid]['children'][id] = rest_re
                    queue_child_dict[id] = rest[pid]['children'][id]['children']

                else:

                    rest_re = rest.pop(re)
                    queue_queue['children'][id] = rest_re
                    queue_child_dict[id] = rest_re['children']
        # pprint(queue_queue)

        def add_tree_child_item(pitme,children):
            for child in children['children'].values():
                item = TreeWidgetItem(pitme)
                # print(child['data'])
                item.setText(0,child['data']['name'])
                item.model_data = child['data']
                add_tree_child_item(item,child)

                item.setBackground(0,QBrush(QColor("#CEC1C4")))
                item.typelc = 'l'
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        for fchild in queue_queue['children'].values():
            item = TreeWidgetItem(self)

            item.setText(0,fchild['data']['name'])

            # 1 字典 2 model
            item.model_data = fchild['data']
            add_tree_child_item(item,fchild)

            item.setBackground(0,QBrush(QColor("#CEC1C4")))
            item.typelc = 'l'
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        self.setcontent(labels,contents)
    # 
    def itemDoubleClicked_connect(self,item,column):
        # sender = self.sender()
        # print(item.text(column))
        # print(11)
        # print(item.text(column))
        # print(item.isExpanded())
        item.setExpanded( item.isExpanded())




class LabelTree(QTreeWidget):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.setColumnCount(1)
        self.setHeaderHidden(True)


        self.get_Labels()
        self.h_sort()

        # self.setSelectionMode
        # self.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.setDragDropMode(QAbstractItemView.DragDrop)
        # self.setDragEnabled(True)
        # self.setAcceptDrops(True)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.InternalMove) 
        self.setSelectionMode(QAbstractItemView.ExtendedSelection) 




        self.itemDoubleClicked.connect(self.itemDoubleClicked_connect)
        self.itemChanged.connect(self.itemChanged_connect)
        # self.itemClicked.connect(self.itemClicked_connect)



    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Insert):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                # self.close()
                pass
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.add_child_tem()
            else:
                self.add_next_item()


    def dragMoveEvent(self, event):
        self.sitems = self.selectedItems()
        super().dragMoveEvent(event)
        # event.accept()

    def dropEvent(self, event):
        super().dropEvent(event)
        for item in self.sitems:
            if item.parent():
                pobj = item.parent().model_data['object']
                if item.model_data['pid'] != pobj.id:
                    # print(1,item.model_data['name'],item.parent().model_data['name'])
                    item.model_data['pid'] = pobj.id
                    obj = item.model_data['object']
                    obj.pid = pobj.id
                    obj.save()

                queue = []
                for i in range(item.parent().childCount()):
                    queue.append(str(item.parent().child(i).model_data['object'].id))
                if pobj.queue:
                    queue = (','.join(queue),pobj.queue.split('|')[1])
                else:
                    queue = (','.join(queue),'')
                queue = '|'.join(queue)
                pobj.queue = queue
                # print(pobj.name,pobj.id,pobj.queue)
                pobj.save()




            else:
                if item.model_data['pid'] != 1:
                    # print(0,item.model_data['name'],'xx')
                    item.model_data['pid'] = 1

                    obj = item.model_data['object']
                    obj.pid = 1
                    obj.save()




    # def itemClicked_connect(self,item,column):
    #     item.setFlags(Qt.ItemIsEditable)

    def itemChanged_connect(self,item,column):

        if hasattr(item,'model_data') and item.model_data['name'] != item.text(0):
            obj = item.model_data['object']
            obj.name = item.text(0)
            item.model_data['name'] = item.text(0)
            obj.save()

    def itemDoubleClicked_connect(self,item,column):
        # sender = self.sender()
        # print(item.text(column))
        item.setExpanded(not item.isExpanded())

    def set_mself(self,mself):
        self.mself = mself

    def get_currentItem_model_data(self):
        return self.currentItem().model_data


    # [ name ,pid ,queue ,grade]

    def get_Labels(self):

        labels = models.Label.objects.all().order_by('id')
        labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))
        labels = list(labels)
        queue_queue = {'data':None,'children':{}}
        queue_child_dict = {1:queue_queue['children']}
        rest = {}

        
        c = 0
        for i in range(len(labels)):
            la = labels[i]
            labels_values[i]['object'] = la




            id = labels_values[i]['id']
            name = labels_values[i]['name']
            pid = labels_values[i]['pid']
            queue = labels_values[i]['queue']
            grade = labels_values[i]['grade']
            create_date = labels_values[i]['create_date']

            if pid == -1:
                queue_queue['data'] = labels_values[i]
            elif pid == 1:
                queue_queue['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_queue['children'][id]['children']
            elif pid in queue_child_dict:
                queue_child_dict[pid][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_child_dict[pid][id]['children']
            elif pid in rest:
                rest[pid]['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = rest[pid]['children'][id]['children']
            else:
                rest[id] = {'data':labels_values[i],'children':{}}
        print('rest 是否可以取消字典改为 set')


        while rest:
            for re in rest.copy():
                id = rest[re]['data']['id']
                name = rest[re]['data']['name']
                pid = rest[re]['data']['pid']
                queue = rest[re]['data']['queue']
                grade = rest[re]['data']['grade']
                create_date = rest[re]['data']['create_date']
                if pid in queue_child_dict:
                    rest_re = rest.pop(re)
                    queue_child_dict[pid][id] = rest_re
                    queue_child_dict[id] = queue_child_dict[pid][id]['children']
                    
                elif pid in rest:
                    rest_re = rest.pop(re)
                    rest[pid]['children'][id] = rest_re
                    queue_child_dict[id] = rest[pid]['children'][id]['children']

        # pprint(queue_queue)

        def add_tree_child_item(pitme,children):
            for child in children['children'].values():
                item = TreeWidgetItem(pitme)
                # print(child['data'])
                item.setText(0,child['data']['name'])
                item.model_data = child['data']
                add_tree_child_item(item,child)

        for fchild in queue_queue['children'].values():
            item = TreeWidgetItem(self)
            item.setText(0,fchild['data']['name'])

            # 1 字典 2 model
            item.model_data = fchild['data']
            add_tree_child_item(item,fchild)

    def h_sort(self):
        def _sort(item):
            #首项的顺序先不排序
            iddict = {}
            for i in range(item.childCount()):
                citem = item.child(i)
                _sort(citem)
                iddict[citem.model_data['object'].id] = citem
            queue = item.model_data['object'].queue
            if queue and queue.split('|')[0]:
                queue = queue.split('|')[0].split(',')
            for j in reversed(queue):
                j = int(j)
                citem = iddict.get(j)
                if not citem:
                    continue
                item.removeChild(citem)
                item.insertChild(0,citem)
                
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            _sort(item)

    def add_child_tem(self):
        item = self.currentItem()
        nitem = TreeWidgetItem()
        item.addChild(nitem)
        pid = item.model_data['id']

        obj = models.Label.objects.create(name='new',pid=pid,grade=10)
        nitem.setText(0,'new')
        nitem.model_data = {'id':obj.id,
                            'name':obj.name,
                            'pid':obj.pid,
                            'queue':obj.queue,
                            'grade':obj.grade,
                            'create_date':obj.create_date,
                            'object':obj
                            }
        # nitem.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)
        self.setCurrentItem(nitem)
        self.editItem(nitem,0)


    def add_next_item(self):
        item = self.currentItem()
        nitem = TreeWidgetItem()
        if not item:
            self.addTopLevelItem(nitem)
            pid=1
        elif item.parent():
            item.parent().insertChild(item.parent().indexOfChild(item)+1,nitem)
            pid = item.parent().model_data['id']
        else:
            self.insertTopLevelItem(self.indexOfTopLevelItem(item)+1,nitem)
            pid = 1

        obj = models.Label.objects.create(name='new',pid=pid,grade=10)
        nitem.setText(0,'new')
        nitem.model_data = {'id':obj.id,
                            'name':obj.name,
                            'pid':obj.pid,
                            'queue':obj.queue,
                            'grade':obj.grade,
                            'create_date':obj.create_date,
                            'object':obj
                            }
        # nitem.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled)
        self.setCurrentItem(nitem)
        self.editItem(nitem,0)


    # def additem(self):
    #     root = TreeWidgetItem(self)
    #     root.setText(0,'333')

    #     root.setExpanded

    #     qti1 = TreeWidgetItem(root)
    #     qti1.setText(0,'111')
    #     root.addChild(qti1)

    #     self.itemDoubleClicked.connect(self.edititem)

class PushButton(QPushButton):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.model_data = None
        

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show_label_lst = []
        self.initUI()
        self.lineedit_textchanged_time = None
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.connect_db) 
        self.timer.start(1000 * 60 * 30)

    def connect_db(self):
        print('每半小时连接一次服务器',end='\r')
        x = models.Content.objects.filter(id = -100).count()
        print('每半小时连接一次服务器 成功连接 '+ str(x))

    def initUI(self):

        hbox = QHBoxLayout()
        self.content_layout = QVBoxLayout()
        vbox_left = QVBoxLayout()
        vbox_right = QVBoxLayout()

        widget_left=QWidget()
        widget_left.setLayout(vbox_left)

        widget_right=QWidget()
        widget_right.setLayout(vbox_right)

        vbox_right.addLayout(self.content_layout)

        self.tree = MyTree()
        self.tree.set_mself(self)
        self.tree.set_mysender(self.label_tree_clicked)
        self.textEdit = TextEdit()
        self.le1 = QLineEdit()
        self.le1.returnPressed.connect(self.search_models)

        # self.cl_bt_bt = QLabel('标签')
        
        cl_bt_hbox = QHBoxLayout()
        self.cl_bt_le = QLineEdit('内容')
        self.cl_bt_bt = QPushButton('新建')
        self.cl_bt_bt.clicked.connect(self.cl_bt_bt_clicked)
        # self.cl_bt_le.textChanged.connect(self.cl_bt_le_textChanged)
        cl_bt_hbox.addWidget(self.cl_bt_le)
        # cl_bt_hbox.addWidget(self.cl_bt_bt)
        # self.content_layout = 





        vbox_left.addWidget(self.le1)
        vbox_left.addWidget(self.tree)
        vbox_right.addWidget(self.textEdit)

        self.content_layout.addLayout(cl_bt_hbox)




        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(widget_left)
        splitter1.addWidget(widget_right)
        splitter1.setSizes((150,300))

        hbox.addWidget(splitter1)


        widget=QWidget()
        widget.setLayout(hbox)
        self.setCentralWidget(widget)


        self.setGeometry(200, 200, 800, 600)






        # 20181029 23:24:23 完成基本功能
        version = '0.9.1'

        # 20181030 10:25:16 fix bug
        version = '0.9.2'

        # 20181030 11:54:29 fix bug
        version = '0.9.3'

        # 20181105 17:30:48 断线重新运行
        version = '0.9.4'

        # 20181105 17:30:48 增加ctrl+s 保存
        version = '0.9.5'

        self.setWindowTitle('know '+version)



        self.content_layout_current_id = None

        menubar = self.menuBar()
        self.file = menubar.addMenu('&File')

        # set shortcut
        self.set_shortcut('save','Ctrl+S',self.save_text)
        self.set_shortcut('embark','alt+q',self.exec_test)
        self.set_shortcut('embark2','alt+e',self.embark_shortcut )

        self.show()
        self.show_labels()

    # def __del__(self):
    #     print('xg')

    # def closeEvent(self,event):
    #     sys.exit(app.exec_())

    def set_shortcut(self,name,shortcut,fun):
        save = QAction(QIcon(''),  name,  self)
        save.setShortcut(shortcut)
        save.setStatusTip(name + ' application')
        save.triggered.connect(fun)

        self.file.addAction(save)

    def save_text(self):
        self.show_labels_pre()

    def embark_shortcut(self):
        print(11)
        cobj = models.Content.objects.get(name='know快捷键')
        res1 = re.findall(r'\<sublime\>([\w\W]+)\<sublimeend\>',cobj.text)[0].strip()
        res1 = [   s.split('|')          for s in res1.split('\n')]
        res1 = dict(res1)

        res2 = re.findall(r'\<python\>([\w\W]+)\<pythonend\>',cobj.text)[0].strip()
        res2 = [   s.split('|')          for s in res2.split('\n')]
        res2 = dict(res2)

        res = (res1,res2)
        return res

    def exec_test(self):
        print(1111111)
        filename = 'myexec.py'
        with open(filename,'r',encoding='utf-8') as f:
            data = f.read()
        try:
            exec(data)
        except Exception:
            traceback.print_exc()





    def show_labels_pre(self):
        if self.content_layout_current_id:
            obj = models.Content.objects.get(id = self.content_layout_current_id)
            name = self.cl_bt_le.text()
            text = self.textEdit.toPlainText()

            change = False
            if name != obj.name:
                change = True
                obj.name = name
                for item in self.tree.content_item_dict[obj.id]:
                    try:
                        item.setText(0,name)
                    except RuntimeError:
                        print('RuntimeError again')
                        pass




            if text != obj.text:
                change = True
                obj.text = text
            if change:
                obj.save()
                print('数据保存完成')


    def show_labels(self):
        # 设置 textedit 和 cl_bt_le 的文字 并生成标签
        for bt in self.show_label_lst:
            sip.delete(bt)
        self.show_label_lst = []

        if self.content_layout_current_id:
            obj = models.Content.objects.get(id = self.content_layout_current_id)
            self.cl_bt_le.setText(obj.name)
            self.textEdit.setText(obj.text)
            createddate = obj.create_date + datetime.timedelta(hours=8)
            createddate = createddate.strftime('%Y-%m-%d %H:%M:%S')
            self.statusBar().showMessage(str(obj.id) + ' ' + createddate)


            labs = obj.labels.all()
            strr = labs.values('name')
            strr = [ s['name'] for s in strr]
            

            labs = list(labs)

            labs = [ {'id':la.id,
                    'name':la.name,
                    'pid':la.pid,
                    'queue':la.queue,
                    'grade':la.grade,
                    'create_date':la.create_date,
                    'object':la
                    } for la in labs]
        else:
            strr = []
            labs = []
        # print(self.content_layout_current_id)

        strr.append('新建')
        labs.append(None)
        sumwidth = self.textEdit.width()

        content_layout_queue = [0,1] 
        # strr,strrf1 = strr[1:],strr[0]
        # strr.append(strrf1)
        # print(strr)
        # print(len(strr))
        
        bttemp = QPushButton('内asds容')
        sumlong = bttemp.fontMetrics().width(strr[0]) + 20
        for i in range(1,len(strr)):
            sumlong += bttemp.fontMetrics().width(strr[i]) + 20
            # print(bttemp.fontMetrics().width(strr[i]) + 20)
            if sumlong>sumwidth:
                # print(sumlong- bttemp.fontMetrics().width(strr[i]) + 20,sumlong,sumwidth)
                sumlong = bttemp.fontMetrics().width(strr[i]) + 20
                content_layout_queue.append(i + 1)
            else:
                content_layout_queue[-1] = i + 1
            # print(11,content_layout_queue)

        sip.delete(bttemp)
        # print(content_layout_queue)

        # content_layout_queue.insert(0,-1)
        # print(content_layout_queue)
        for i in range(1,len(content_layout_queue)):
            layout = QHBoxLayout()
            self.content_layout.insertLayout(self.content_layout.count()-1,layout)
            # print(content_layout_queue[i] - content_layout_queue[i-1] + 1)
            for j in range(content_layout_queue[i] - content_layout_queue[i-1]):
                # print(j)
                bt = PushButton(strr[ j + content_layout_queue[i-1]])
                width = bt.fontMetrics().width(strr[ j + content_layout_queue[i-1]]) + 10
                bt.setMinimumSize(width,20)
                bt.setMaximumSize(width,20)
                bt.clicked.connect(self.addlabel)
                # print(j + content_layout_queue[i-1])
                bt.model_data = labs[j + content_layout_queue[i-1]]
                # bt.isnew = True
                layout.addWidget(bt)
                self.show_label_lst.append(bt)

            self.show_label_lst.append(layout)
            layout.addStretch()

    def cl_bt_bt_clicked(self):
        self.show_labels_pre()
        sender = self.sender()

        self.cl_bt_le.setText('new')
        self.textEdit.setText('new')
        name = self.cl_bt_le.text()
        text = self.textEdit.toPlainText()
        cobj = models.Content.objects.create(name=name,text=text)
        self.content_layout_current_id = cobj.id
        self.show_labels()

        item = TreeWidgetItem(self.tree)
        item.setText(0,cobj.name)
        item.model_data = {
                            'id':cobj.id,
                            'name':cobj.name,
                            'text':cobj.text,
                            'object':cobj,
        }




        # if sender.text() == '新建':
        #     sender.setText('确定')
        # elif sender.text() == '确定':
        #     sender.setText('新建')
    
    # def cl_bt_le_textChanged(self):

        
        
    #     self.timer.start(4000)
    #     sender = self.sender()
    #     print(sender)
    #     self.lineedit_textchanged_time = time.time()





    # def cl_bt_le_textChanged_finished(self):
    #     # if self.lineedit_textchanged_time + 3.5 < time.time():
    #     self.timer.stop()
    #     print('修改',self.cl_bt_le.text())
    #     if self.content_layout_current_id:
    #         obj = models.Content.objects.get(id = self.content_layout_current_id)
    #         if obj.name != self.cl_bt_le.text():
    #             obj.name = self.cl_bt_le.text()
    #             self.search_models()



    def addlabel(self):

        self.show_labels_pre()

        self.bt_sender = self.sender()
        
        self.dia = QDialog(self)
        vbox = QVBoxLayout()
        self.dia.setLayout(vbox)
        self.ltree = LabelTree()

        self.ltree.set_mself(self)



        ok_bt = QPushButton('确定')
        ok_bt.clicked.connect(self.dia_ok_bt_clicked)

        cancel_bt = QPushButton('取消')
        cancel_bt.clicked.connect(self.dia_cancel_bt_clicked)

        hbox = QHBoxLayout()
        vbox.addWidget(self.ltree)
        hbox.addWidget(ok_bt)
        hbox.addWidget(cancel_bt)
        vbox.addLayout(hbox)

        if self.bt_sender.model_data:
            items = self.ltree.findItems(self.bt_sender.text(),Qt.MatchRecursive,0)
            for item in items:
                if self.bt_sender.model_data['id'] == item.model_data['id']:
                    self.ltree.setCurrentItem(item)
                    self.ltree.scrollToItem(item,QAbstractItemView.EnsureVisible)
                    break

        # ui->TW_1->setCurrentItem(ptems.at(0));
        # ui->TW_1->scrollToItem(ptems.at(0),QAbstractItemView::EnsureVisible);

        # self.dia.show()
        self.dia.exec()
        # ql.exec_()


    def dia_ok_bt_clicked(self):

        obj = models.Content.objects.get(id=self.content_layout_current_id)
        if self.bt_sender.model_data:
            # print(self.bt_sender.model_data['object'])
            # print(type(self.bt_sender.model_data['object']))
            obj.labels.remove(self.bt_sender.model_data['object'])




        obj.labels.add(self.ltree.get_currentItem_model_data()['object'])

        self.show_labels()
        self.dia.close()


    def dia_cancel_bt_clicked(self):
        obj = models.Content.objects.get(id=self.content_layout_current_id)
        if self.bt_sender.model_data:




            button=QMessageBox.question(self,"Question",  
                                               self.tr("是否确认删除?"),  
                                               QMessageBox.Ok|QMessageBox.Cancel,  
                                               QMessageBox.Ok)  
            if button==QMessageBox.Ok:  
                obj.labels.remove(self.bt_sender.model_data['object'])
                self.show_labels()
            

        # 
        self.dia.close()



        #     bt = PushButton('新建')
        #     width = bt.fontMetrics().width('新建') + 10
        #     bt.setMinimumSize(width,20)
        #     bt.setMaximumSize(width,20)
        #     bt.clicked.connect(self.addlabel)

        # self.bt_sender.model_data = self.ltree.get_currentItem_model_data()
        # self.bt_sender.setText(self.bt_sender.model_data['name'])
        # width = self.bt_sender.fontMetrics().width(self.bt_sender.model_data['name']) + 10
        # self.bt_sender.setMinimumSize(width,20)
        # self.bt_sender.setMaximumSize(width,20)

    def label_tree_clicked(self,id):

        self.show_labels_pre()
        self.content_layout_current_id = id
        self.show_labels()

    def search_models_none(self):
        def labels_children(labels):
            ls = set()
            for l in labels:
                ls |= set([l.id for l in models.Label.objects.filter(pid=l)])
            return labels | labels_children(ls) if ls else labels

        text = self.le1.text()

        objsall = models.Content.objects.filter(id=-1111)
        if not text:
            labelobjs = None
        else:
            for te in text.split(' '):
                cobjs = models.Content.objects.filter(Q(name__contains=te) | Q(text__contains=te) ) #| Q(labels__name__contains=te)

                labels = models.Label.objects.filter(name__contains=te)

                labels = labels_children(set([l.id for l in labels]))
                # cobjs |= models.Content.objects.filter(labels__id__in=labels)
                
                labelobjs = models.Label.objects.filter(id__in=labels)

                if objsall:
                    objsall = objsall & cobjs
                else:
                    objsall = cobjs
            objsall = objsall.distinct()
        self.tree.setitem(labelobjs,objsall) #labelobjs


    def search_models(self):

        text = self.le1.text()
        if text[0] == '#':
            cobj = models.Content.objects.get(name='know_setting')
            
            res = re.findall(r'\<knowset\>([\w\W]+)\<knowsetend\>',cobj.text)[0].strip()
            res = [   s.split(' ')          for s in res.split('\n')]
            res = dict(res)
            res = res.get(text[1:])
            if res:
                # cobjtemp = models.Content.objects.get(id=res)
                try:
                    models.Content.objects.get(id=res)
                    self.label_tree_clicked(res)
                except models.Content.DoesNotExist:
                    pass
            return

        elif text[0] == '@':
            cobj = models.Content.objects.get(name='know_setting')
            res = re.findall(r'\<knowlabelname\>([\w\W]+)\<knowlabelnameend\>',cobj.text)[0].strip()
            res = [   s.split(' ')          for s in res.split('\n')]
            res = dict(res)
            res = res.get(text[1:])
            if res:
                self.le1.setText(res)


        def get_contents_by_textlst(textlst):

            def get_label_children(label_id_set):
                llen = len(label_id_set)
                for i in self.labeldict:
                    label = self.labeldict[i]
                    if label.pid in label_id_set:
                        label_id_set.add(label.id)
                if llen != len(label_id_set):
                    get_label_children(label_id_set)

            content_id_set_by_label_lst = []
            content_id_set_by_text_lst = []
            content_id_set_by_true_text_lst = []
            label_id_set_lst = []
            for text in textlst:
                # content_id_set_by_label = set()
                content_id_set_by_text = set()
                # content_id_set_by_true_text = set()
                label_id_set = set()
                for i in self.labeldict:
                    label = self.labeldict[i]
                    if text in label.name:
                        label_id_set.add(label.id)


                get_label_children(label_id_set)

                # pprint(label_id_set)

                # for id_ in label_id_set:
                #     content_id_set_by_label |= self.get_contents_by_label.get(id_,set())

                for id_,content in self.contentdict.items():
                    if text in content.name:
                        content_id_set_by_text.add(id_)
                    elif text in content.text:
                        content_id_set_by_text.add(id_)



                # content_id_set_by_label_lst.append(content_id_set_by_label)
                content_id_set_by_text_lst.append(content_id_set_by_text)
                # content_id_set_by_true_text_lst.append(content_id_set_by_true_text)
                label_id_set_lst.append(label_id_set)



            content_id_set_by_text = reduce(lambda x,y:x & y,content_id_set_by_text_lst)
            # content_id_set_by_label = reduce(lambda x,y:x & y,content_id_set_by_label_lst)
            # content_id_set_by_true_text = reduce(lambda x,y:x & y,content_id_set_by_true_text_lst)
            label_id_set = reduce(lambda x,y:x & y,label_id_set_lst)

            # print(content_id_set_by_label)
            # print('是不是可以把 content_id_set_by_label 删除')
            
            return content_id_set_by_text,label_id_set




        def set_all_data():

            def set_content_labels():
                cursor = connection.cursor()
                sql = 'select content_id,label_id from data_content_labels;'
                cursor.execute(sql)
                rows = cursor.fetchall()

                self.get_labels_by_content = {}
                self.get_contents_by_label = {}

                for row in rows:
                    labels_set = self.get_labels_by_content.get(row[0])
                    if not labels_set:
                        self.get_labels_by_content[row[0]] = {row[1]}
                    else:
                        labels_set.add(row[1])

                    contents_set = self.get_contents_by_label.get(row[1])
                    if not contents_set:
                        self.get_contents_by_label[row[1]] = {row[0]}
                    else:
                        contents_set.add(row[0])

            labelall = models.Label.objects.all()
            contentall = models.Content.objects.all()
            
            self.labeldict = {}
            for label in labelall:
                self.labeldict[label.id] = label
            
            self.contentdict = {}
            for content in contentall:
                self.contentdict[content.id] = content

            
            set_content_labels()



        set_all_data()
        textlst = self.le1.text().split(' ')
        # pprint(self.get_contents_by_label)
        content_id_set_by_text,label_id_set = get_contents_by_textlst(textlst)
        # label_id_set = get_labels_by_content_id_set(content_id_set_by_label)

        self.tree.set_label_treeitems(label_id_set,self)

        self.tree.setcontent(label_id_set,content_id_set_by_text,self)
        # self.tree.setcontent(set(),content_id_set_by_true_text,self,False)






# printold = print

# def print(*args,**kw):
#     global GTIMES
#     printold(str(args),*args,**kw)

#     T = time.time()
#     printold('------spend time:%ss' %  (T - GTIMES))
#     GTIMES = T



if __name__ == '__main__':
    content_id_set_lst = [{1,2,3},{3,4,5},{1,8,3}]
    content_id_set = reduce(lambda x,y:x & y,content_id_set_lst)
    print(content_id_set)
    # labelall = models.Label.objects.all()
    # contentall = models.Content.objects.all()
    # labelall = list(labelall)
    # for x in contentall.labels.all():
    #     print(x)






    # labeldict = {}
    # for label in labelall:
    #     labeldict[label.id] = label

    # def get_contents_by_textlst(text):
    #     content_id_set = set()
    #     label_id_set = set()
    #     for i in labeldict:
    #         label = labeldict[i]
    #         if text in label.name:
    #             label_id_set.add(label.id)
    #     get_label_children(label_id_set)
    #     return label_id_set

    # def get_label_children(label_id_set):
    #     llen = len(label_id_set)
    #     for i in labeldict:
    #         label = labeldict[i]
    #         if label.pid in label_id_set:
    #             label_id_set.add(label.id)
    #     if llen != len(label_id_set):
    #         get_label_children(label_id_set)
    # label_id_set = get_contents_by_textlst('eva')
    # for i in label_id_set:
    #     print(labeldict[i].name)


    # def bbb():
    #     # a = sys._getframe()
    #     aaa()
    # def aaa():
    #     a = sys._getframe().f_back.f_back.f_lineno
    #     print(a)
    #     print(sys._getframe().f_trace )

    # print(sys._getframe())
    # # print(type(sys._getframe().f_lasti))
    # c = sys._getframe()
    # a = c
    # print(a.f_lasti)
    # print(a.f_lineno)
    # bbb()
    

    # def get_variable_name(x)->str:
    #     for k,v in locals().items():
    #         if v is x:
    #             return k

    # def print_var(x)->None:
    #     print(get_variable_name(x),'=',x)

    # a = 1
    # print_var(a)


    # try:
    #     aacc
    # except Exception as e:
    #     print(11)
    #     pass
    # print(sys._getframe().f_trace )




    # aa = models.Label.objects.filter(id=1)[0]
    # print(aa)
    # print(aa.name)
    # aa.name ='333'
    # aa.save()

    # bb = models.Label.objects.filter(name='333')[0]
    # print(bb.name)

    # print(aa == bb)




    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
