
import sys
import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame,QSplitter, QStyleFactory, QApplication
from PyQt5.QtWidgets import QTreeWidget, QTextEdit, QMainWindow, QTreeWidgetItem, QLineEdit,QPushButton, QLabel,QMenu
from PyQt5.QtWidgets import QDialog, QShortcut, QAbstractItemView, QAction ,QMessageBox
from PyQt5.QtCore import Qt, QTimer, QRegExp, QThread
from PyQt5.QtGui import QKeySequence, QIcon, QBrush, QColor, QFont, QTextDocument, QTextCharFormat ,QTextDocumentFragment ,QTextOption ,QClipboard,QCursor


from gl.gl import myexec,get_computer_info,CURRENTURL,open, TryClass, tryruntime


bios = get_computer_info

if bios[0] == 0:
    file_exe = r'start /b F:\sublime\SublimeText_XP85\sublime_text.exe'
elif bios[0] == 1:
    file_exe = r'start /b E:\Desktop\SublimeText3\sublime_text.exe'
elif bios[0] == 2:
    file_exe = r'start /b H:\Desktop\lj\sublimetextbuild3143\sublime_text'
        
from pprint import pprint
import sip
from hmysql import Q,timezone,      LABEL_FIELDS,CONTENT_FIELDS,HGFILE_FIELDS,MyModels,MyQuery,save_all_data,      Label,Content ,runn
import time
from django.db import connection
from functools import reduce
import re
import traceback
import pyperclip
import datetime
import pickle
from func.hcalendar import HCalendar
import subprocess
import screen_capture
from multiprocessing import Process,Pipe
from func.passworkdialog import PasswdDialog
from func.hgcrypto import mmCrypto
from func.myexcept import *
from func.labelhistory import LabelHistory
from xpinyin import Pinyin
from func.know001_follow_know import single_windows, follow_know_windows
from func.know002_search_again import know002_search_again

# sys.setrecursionlimit(150) # set the maximum depth as 1500



# from main import models



GTIMES = time.time()


#-------------------重写formysql-------------------
def gettype(obj):
    if "<class 'hmysql.MyModels'>" == str(type(obj)):
        obj = obj.model
    if isinstance(obj, Label) or str(obj) == "<class 'data.models.Label'>":
        return 'l'
    elif isinstance(obj, Content) or str(obj) == "<class 'data.models.Content'>":
        return 'c'
    print(obj,'错误的参数类型')
    return
#-------------------重写formysql-------------------

class ConnThread(QThread):
    def __init__(self,mself):
        super().__init__()
        self.mself = mself

    def run(self):
        lst = []
        # REPLACE = {}
        while True:
            conn1, self.mself.conn = Pipe()
            filename = os.path.join(CURRENTURL,'gl','errbak.dat')
            if os.path.exists(filename):
                with open(filename,'rb') as f:
                    lst = pickle.load(f)
                    # REPLACE = pickle.load(f)
                pprint(lst)
                if input('如果读取数据输入y') in 'yY':
                    os.remove(filename)
                else:
                    lst = []
            Process(target=runn,args = (conn1,self.mself.conn,lst)).start()
            lst = []
            conn1.close()

            while True:
                res = self.mself.conn.recv()
                if res == 'err':
                    with open(filename,'rb') as f:
                        lst = pickle.load(f)
                        # REPLACE = pickle.load(f)
                    os.remove(filename)
                    break


            self.mself.conn.close()

class PushButton(QPushButton):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.model_data = None
        # 窗口标题
        self.setWindowTitle(' ')
        # 定义窗口大小
        self.resize(400, 400)
        # 将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 创建QMenu信号事件
        self.customContextMenuRequested.connect(self.showMenu)

    def showMenu(self, pos):
        if not self.model_data:
            return
        obj = self.model_data['object']
        pid = obj.pid

        strlst = [obj.name]
        while pid != 1:
            la = MyModels(Label,None,pid)
            pid = la.pid
            strlst.append(la.name)

        self.contextMenu = QMenu(self)

        # pprint(dir(self.contextMenu))

        for s in strlst:
            t = self.contextMenu.addAction(s)
            t.triggered.connect(self.Event)

        self.contextMenu.exec_(QCursor.pos()) #在鼠标位置显示

    def Event(self):
        # QMessageBox.information(self, "提示：",'      您选择了'+self.sender().text())
        self._zself.le1.setText(self.sender().text())
        self._zself.search_models()
        # print(self.model_data)

    def setzself(self,zself):
        self._zself = zself

class TextEdit(QTextEdit):
    def __init__(self, *arg,mself=None, **kw):
        super().__init__(*arg, **kw)
        self.mself = mself
        self.__func_arg__()
        # self.setWordWrapMode(QTextOption.NoWrap)
        self.setFrameStyle(QFrame.WinPanel)
        self.ismyInsertPlainText = True
        # self.password = None
        self.mmcrypto = mmCrypto()
        self.another_textedit = QTextEdit()

    def __func_arg__(self):
        self.git_cwd = 'all'
        self.git_pathdict = {'evaluate':r'F:\mygit\python\evaluate',
                             'know':r'F:\my\P028_knowledge_system\knowqt',
                                }

    def insertFromMimeData(self,source):
        # print('insertFromMimeData')
        # return myexec()
        # 
        # 
        os.path.join(CURRENTURL,'kqj','data','static','pic')
        if source.hasImage():
            xx = source.imageData()
            hgfileid = models.HGFile.objects.create(name='qt')

            path = os.path.join('static','pic',str(hgfileid)+'.png')

            # hgfile.path = path

            zz = xx.save(os.path.join(CURRENTURL,'kqj','data',path))
            fname = os.path.join(CURRENTURL,'kqj','data',path)
            
            fragment = QTextDocumentFragment.fromHtml("<img src='%s'>" % fname)
            self.textCursor().insertFragment(fragment);

            self.insertPlainText('<hgpic=%s>\n' % hgfileid)
        elif self.ismyInsertPlainText:
            self.insertPlainText(source.text())
        else:
            QTextEdit.insertFromMimeData(self, source)

    def canInsertFromMimeData(self,source):
        print('canInsertFromMimeData')
        # return myexec()
        return QTextEdit.canInsertFromMimeData(self, source)

    def dropEvent(self, e):
        # return myexec()
        print('dropevent')

        emine = e.mimeData()
        if emine.hasUrls():
            print(e.mimeData().text(),33333333333)
        tx = e.mimeData().text()
        if tx.startswith('file:///'):
            tx = tx[8:]
            print(tx)

        else:
            QTextEdit.dropEvent(self, e)

    def mouseDoubleClickEvent(self, event):
        try:
            x = self.textCursor()
            self.moveCursor(x.StartOfBlock,x.MoveAnchor)
            self.moveCursor(x.EndOfBlock,x.KeepAnchor)
            zzz = self.textCursor().selectedText().strip()
            if zzz.startswith('http://') or zzz.startswith('https://'):
                os.startfile(zzz.strip())
                return




            res = zzz.split('|')
            if len(res) >= 2:
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
                        f.write('python ' + file_name)
                    os.chdir(os.path.dirname(file_name))
                    os.startfile(r'F:\my\P028_knowledge_system\knowqt\myfn\h10_try_command.py')

                    # file_name = res[1]
                    # file_name = "C:\\Windows\\System32\\cmd"

                    # filename = 'F:\\my\\F00_myfn\\h10_try_command_file.txt'
                    # with open(filename,'w',encoding='utf-8') as f:
                    #     f.write(file_name)
                    # os.chdir(os.path.dirname(file_name))
                    # os.startfile('F:\\my\\F00_myfn\\h10_try_command.py')

                elif res[0] == 'finish':
                    self.setText(self.mself.hc.addhistory(self.toPlainText()))

                elif res[0] == 'search':
                    text = self.mself.le1.text()
                    res = res[1:]
                    for i,r in enumerate(res):
                        r = r.strip().split()[0]
                        if text == r:
                            i += 1
                            if i >= len(res):
                                i = 0
                            # print(res,i)
                            r = res[i].strip().split()[0]
                            break
                    else:
                        r = res[0].strip().split()[0]
                    # print(r)
                    self.mself.le1.setText(r)
                    self.mself.search_models()

                elif res[0] == 'http':
                    os.startfile(res[1].strip().split()[0])
                    

                elif res[0] == 'content':
                    r = res[1].strip().split()[0]
                    if r.isdigit():
                        r = int(r)
                        self.mself.label_tree_clicked(r)
                        return

                elif res[0] == 'textedit_nowrap':
                    if self.wordWrapMode() == QTextOption.WordWrap:
                        self.setWordWrapMode(QTextOption.NoWrap)
                    else:
                        self.setWordWrapMode(QTextOption.WordWrap)

                    

                elif res[0] == 'copy_type':
                    if self.frameStyle() == 54:
                        self.setFrameStyle(QFrame.WinPanel)
                        self.ismyInsertPlainText = True
                    elif self.frameStyle() == 3:
                        self.setFrameStyle(54)
                        self.ismyInsertPlainText = False

                else:
                    super().mouseDoubleClickEvent(event)
            else:
                super().mouseDoubleClickEvent(event)


        except:
            traceback.print_exc()
        # super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event):
        # return myexec()
        # print(event.key())
        # 
        
        if event.key() == Qt.Key_Tab:
            'table'
            if QApplication.keyboardModifiers()==Qt.ControlModifier:
                print('alt table')
            else:
                st = self.textCursor().selectedText()
                if not st:
                    self.insertPlainText('    ')
                else:
                    tc = self.textCursor()
                    # self.moveCursor(tc.PreviousBlock,tc.MoveAnchor)
                    st = self.textCursor().selectedText()
                    # print(st)
                    st = [ '    ' + s for s in st.split('\u2029')]
                    length = len(st)
                    st = '\n'.join(st)
                    self.insertPlainText(st)

                    tc = self.textCursor()
                    if length == 1:
                        self.moveCursor(tc.StartOfBlock,tc.KeepAnchor)
                    else:
                        for _ in range(length-1):
                            self.moveCursor(tc.PreviousBlock,tc.KeepAnchor)
            return None

        elif event.key() == 16777218:
            'shift table'
            tc = self.textCursor()
            st = self.textCursor().selectedText()
            for s in st.split('\u2029'):
                if not s.startswith('    '):
                    break
            else:
                st = [s[4:] for s in st.split('\u2029')]
                length = len(st)
                st = '\n'.join(st)
                self.insertPlainText(st)

                tc = self.textCursor()
                if length == 1:
                    self.moveCursor(tc.StartOfBlock,tc.KeepAnchor)
                else:
                    for _ in range(length-1):
                        self.moveCursor(tc.PreviousBlock,tc.KeepAnchor)
            return None


        elif event.key() == Qt.Key_Backspace:
            'Backspace'
            x = self.textCursor()
            if x.selectedText() == '':
                self.moveCursor(x.PreviousWord,x.KeepAnchor)
                zzz = self.textCursor().selectedText()
                self.setTextCursor(x)
                blank_num = (len(zzz) - len(zzz.rstrip(' ')))
                if blank_num and blank_num % 4 ==0:
                # if zzz.endswith('    '):
                    self.moveCursor(x.PreviousCharacter,x.KeepAnchor)
                    self.moveCursor(x.PreviousCharacter,x.KeepAnchor)
                    self.moveCursor(x.PreviousCharacter,x.KeepAnchor)
                    self.moveCursor(x.PreviousCharacter,x.KeepAnchor)

        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            'Enter'
            if self.mself.cl_bt_le.text() == '<git>' and self.mself.content_layout_current_id == None:

                self.git_keypress_enter()

                return None

            cursor = self.textCursor()
            self.moveCursor(cursor.StartOfBlock,cursor.KeepAnchor)
            zzz = self.textCursor().selectedText()
            x = re.search(r'^\s+',zzz)
            i = 0
            if x:
                i = x.end() -x.start()
                i = i - i % 4
            self.setTextCursor(cursor)
            QTextEdit.keyPressEvent(self,event)
            self.insertPlainText(' '*i)
            return None

        elif event.key() == 70:
            'f'
            if QApplication.keyboardModifiers()==Qt.ControlModifier:
                'ctrl + f'
                history = self.mself.hc.addhistoryex(self.toPlainText())
                cursor = self.textCursor()
                if history[0] == -1:
                    self.moveCursor(cursor.End,cursor.MoveAnchor)
                    self.insertPlainText(history[1])
                    cursor.setPosition(history[2],cursor.MoveAnchor)
                    self.setTextCursor(cursor)
                else:
                    cursor.setPosition(history[0],cursor.MoveAnchor)
                    self.setTextCursor(cursor)
                    self.insertPlainText(history[1])
                    self.moveCursor(cursor.Left,cursor.MoveAnchor)
                return None

        # 
        elif event.key() == 86 and QApplication.keyboardModifiers() == Qt.ControlModifier | Qt.ShiftModifier:
            'ctrl shift v'
            clipboard = QApplication.clipboard()
            s = clipboard.text().replace('\n','')
            self.insertPlainText(s)
            return None


        # about crypto
        # elif event.key() == 77 and QApplication.keyboardModifiers() == Qt.ControlModifier:
        #     self.ctrl_M()

        elif event.key() == 77 and QApplication.keyboardModifiers() == Qt.ControlModifier | Qt.ShiftModifier:
            'ctrl shift M'
            self.shift_M()
            return None

        elif event.key() == 78 and QApplication.keyboardModifiers() == Qt.ControlModifier:
            self.another_textedit.show()
            self.another_textedit.setHtml(self.toHtml())
            return None

        elif event.key() == 16777237:
            '方向下'
            verticalscrollbar_value = self.verticalScrollBar().value()
            cursor = self.textCursor()
            self.moveCursor(cursor.EndOfLine,cursor.MoveAnchor)
            self.moveCursor(cursor.End,cursor.KeepAnchor)
            end = self.textCursor().selectedText()
            if len(end) == 0:
                self.moveCursor(cursor.StartOfLine,cursor.KeepAnchor)
                line = self.textCursor().selectedText()
                if line.lstrip():
                    # print(line.lstrip(),bool(line.lstrip()))
                    x = re.search(r'^\s+',line)
                    i = 0
                    if x:
                        i = x.end() -x.start()
                        i = i - i % 4
                    self.moveCursor(cursor.EndOfLine,cursor.KeepAnchor)
                    self.insertPlainText('\n' + ' '*i)
                    self.setTextCursor(cursor)
                else:
                    self.setTextCursor(cursor)
                    self.moveCursor(cursor.End,cursor.MoveAnchor)
            else:
                self.setTextCursor(cursor)
                self.verticalScrollBar().setValue(verticalscrollbar_value)

        QTextEdit.keyPressEvent(self,event)

    def closeEvent(self, e):
        self.another_textedit.close()

    def ctrl_M(self):
        pwd = PasswdDialog()
        r = pwd.exec_()
        if r:
            self.mmcrypto.set_password(pwd.text)

    def shift_M(self):
        text = '\n<mmde>\n    \n<mm>\n'
        self.insertPlainText(text)

        cursor = self.textCursor()
        for _ in range(6):
            self.moveCursor(cursor.Left,cursor.MoveAnchor)

    def git_keypress_enter(self):
        # return myexec()
        # print(11)
        cursor = self.textCursor()
        self.moveCursor(cursor.StartOfBlock,cursor.MoveAnchor)
        self.moveCursor(cursor.EndOfBlock,cursor.KeepAnchor)
        cmd = self.textCursor().selectedText()
        import subprocess
        if ' git ' in cmd:
            allpath = list(set(self.git_pathdict))
            allpath.insert(0,'all')
            allpath.append('\n')

            git_cwd,cmd = cmd.split(' git ')
            if git_cwd not in allpath:
                return None

            cmd = 'git ' + cmd


            # cmd = 'mkdir 11xxzz'

            if git_cwd == 'all':
                git_cwds = self.git_pathdict.items()
            else:
                git_cwds = [(git_cwd,self.git_pathdict[git_cwd])]

            data = '' 
            for name,cwd in git_cwds:
                os.chdir(cwd)

                if cmd.startswith('git push'):
                    cmd = 'git branch'
                    with subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as f:
                        da = f.stdout.read().decode('utf-8')
                    zz = re.findall(r'\n\* (.*)','\n'+da)[0]
                    cmd = 'git push origin ' + zz
                elif cmd == 'git commit':
                    cmd = "git commit -m'debugbyknow'"

                with subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as f:
                    data += '\n------------------%s-----------------\n' % name
                    data += f.stdout.read().decode('utf-8')
                    data += f.stderr.read().decode('utf-8')


            x = self.mself.textEdit.toPlainText() 
            # print(x)
            x += data + ' '.join(allpath) + git_cwd + ' '
            self.mself.textEdit.setText(x)
            cursor = self.textCursor()
            self.moveCursor(cursor.End,cursor.MoveAnchor)

    def quote_read(self,text,n=1):
        if n > 5:
            print('n 大于 5')
            return
        form = '<quoteb:%s>\n%s\n' + '    '*(n-1) +  '<quotee:%s>\n'

        ids = re.findall(r'<quote:(\d+)>',text)
        if not ids:
            return text
        for i in ids:
            tt = MyModels(Content,None,int(i)).text
            tt = tt.split('\n')
            tt = [ '    '*n + t for t in tt]
            tt = '\n'.join(tt)

            text = text.replace('<quote:%s>'%i,form % (i,tt,i))
        return self.quote_read(text,n+1)

    def quote_recovery(self,text):
        res = re.findall(r'<quoteb:(?P<id>\d+)>([\w\W]+?)<quotee:(?P=id)>(\n)',text)
        for r in res:
            replacetext = '<quoteb:%s>%s<quotee:%s>%s' % (r[0],r[1],r[0],r[2])
            text = text.replace(replacetext,'<quote:%s>' % r[0])
        return text

    def exec_test(self,**kw):
        print('exec_test')
        return myexec()
        clipboard = QApplication.clipboard()
        s = clipboard.text().replace('\n','')
        self.insertPlainText(s)



class TreeWidgetItem(QTreeWidgetItem):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.setFlags(self.flags() | Qt.ItemIsEditable | Qt.ItemIsEnabled)


class MyTree(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(1)
        self.setColumnWidth(0,200)
        self.setColumnWidth(1,30)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.InternalMove) 
        self.setSelectionMode(QAbstractItemView.ExtendedSelection) 

        self.setHeaderHidden(True)

        self.clicked.connect(self.mytree_item_clicked)
        self.itemDoubleClicked.connect(self.itemDoubleClicked_connect)
        self.label_item_dict = {}
        self.content_item_dict = {}

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Insert):
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                # self.close()
                print(22)
            elif QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.add_child_item()
            else:
                self.add_next_item()

    def dragMoveEvent(self, event):
        # self.sitems = self.selectedItems()
        super().dragMoveEvent(event)
        # event.accept()

    def dropEvent(self, event):

        sitems = self.selectedItems()
                
        for item in sitems:
            pitem = item.parent()
            item.oldparent = (pitem, self.indexItem(item), item)

        QTreeWidget.dropEvent(self,event)


        for item in sitems:
            obj = item.model_data['object']
            pobj = item.parent().model_data['object'] if item.parent() else None
            oldpobj = item.oldparent[0].model_data['object'] if item.oldparent[0] else None
            if not item.parent() or gettype(pobj) != 'l':
                self.removeItem(item)
                # print(item.oldparent)
                self.insertItem(*item.oldparent)
            elif gettype(obj) == 'c':
                if oldpobj != pobj:
                    if oldpobj:
                        obj.labels.remove(oldpobj)
                    obj.labels.add(pobj)
                    obj.save()

        for item in sitems:
            if item.parent():
                pobj = item.parent().model_data['object']
                if not item.oldparent[0] or item.oldparent[0].model_data['object'].id != pobj.id:
                    # print(1,item.model_data['name'],item.parent().model_data['name'])
                    obj = item.model_data['object']
                    obj.pid = pobj.id
                    obj.save()

        self.save_queue(item.parent())
                # label_queue = []
                # content_queue = []
                # for i in range(item.parent().childCount()):
                #     if gettype(item.parent().child(i).model_data['object'])=='l':
                #         label_queue.append(str(item.parent().child(i).model_data['object'].id))
                #     else:
                #         content_queue.append(str(item.parent().child(i).model_data['object'].id))



                # queue = (','.join(label_queue),','.join(content_queue))

                # queue = '|'.join(queue)
                # pobj.queue = queue
                # # print(pobj.name,pobj.id,pobj.queue)
                # pobj.save()

    # tree deal
    def indexItem(self,item):
        pitem = item.parent()
        if pitem:
            return pitem.indexOfChild(item)
        else:
            return self.indexOfTopLevelItem(item)

    def insertItem(self, pitem, index, item):
        if pitem:
            pitem.insertChild(index, item)
        else:
            self.insertTopLevelItem(index, item)

    def removeItem(self, item):
        pitem = item.parent()
        if pitem:
            pitem.removeChild(item)
        else:
            self.takeTopLevelItem(self.indexOfTopLevelItem(item))

    def addItem(self, pitem, item):
        if pitem:
            pitem.addChild(item)
        else:
            self.addTopLevelItem(item)

    def children(self,pitem=None):
        if pitem and isinstance(pitem,QTreeWidgetItem):
            return [ pitem.child(i) for i in range(pitem.childCount())]
        else:
            return [ self.topLevelItem(i) for i in range(self.topLevelItemCount())]

    def h_sort(self):
        def _sort(item):
            #首项的顺序先不排序
            label_id_dict = {}
            content_id_dict = {}
            for i in range(item.childCount()):
                citem = item.child(i)


                if gettype(citem.model_data['object'])=='l':
                    label_id_dict[citem.model_data['object'].id] = citem
                else:
                    content_id_dict[citem.model_data['object'].id] = citem

            queue = item.model_data['object'].queue
            label_queue = []
            content_queue = []
            if queue:
                if queue.split('|')[0]:
                    label_queue = queue.split('|')[0].split(',')
                if queue.split('|')[1]:
                    content_queue = queue.split('|')[1].split(',')


            for j in reversed(label_queue):
                j = int(j)
                citem = label_id_dict.get(j)
                if not citem:
                    continue
                item.removeChild(citem)
                item.insertChild(0,citem)

            for j in content_queue:
                j = int(j)
                citem = content_id_dict.get(j)
                if not citem:
                    continue
                item.removeChild(citem)
                item.insertChild(item.childCount(),citem)


            for i in range(item.childCount()):
                citem = item.child(i)
                cobj = citem.model_data['object']
                if gettype(cobj)=='l':
                    citem.setExpanded(bool(self.mself.expanddict.get(cobj.id)))
                    _sort(citem)
                
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            cobj = item.model_data['object']
            item.setExpanded(bool(self.mself.expanddict.get(cobj.id)))
            if gettype(item.model_data['object'])=='l':
                _sort(item)

    def set_mself(self,mself):
        self.mself = mself

    def add_child_item(self):
        pitem = self.currentItem()
        if not gettype(pitem.model_data['object']) == 'l':
            return
        else:
            nitem = TreeWidgetItem(pitem)
            nitem.setFlags(nitem.flags() & ~Qt.ItemIsEditable)
            self.add_tree_citem(pitem,nitem)

    def add_next_item(self):
        bitem = self.currentItem()
        pitem = bitem.parent()
        if not pitem:
            return
        elif gettype(bitem.model_data['object']) == 'l':
            print('ll')
        else:
            nitem = TreeWidgetItem()
            nitem.setFlags(nitem.flags() & ~Qt.ItemIsEditable)
            self.insertItem(pitem, self.indexItem(bitem)+1, nitem)
            self.add_tree_citem(pitem,nitem)

    def add_tree_citem(self,item,nitem):
        mself = self.mself

        mself.show_labels_pre()
        label = item.model_data['object']


        mself.cl_bt_le.setText('new')
        mself.textEdit.setText('new')
        name = mself.cl_bt_le.text()
        text = mself.textEdit.toPlainText()
        cobj = models.Content.objects.create(name=name,text=text)
        cobj.labels.add(label)
        # print(cobj.id)

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

        self.save_queue(nitem.parent())

        if item.text(0) == '<日历>':
            time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
            mself.textEdit.setText('finish|\n\n<time>\nstart|%s\nend|%s\ninterval|1hours/1days/1weeks/1months/1years/1nyear（农历年）\ntimes|\n</time>'%(time_now_str,time_now_str))

    def mytree_item_clicked(self):
        item = self.currentItem()
        obj = item.model_data['object']
        if gettype(obj)=='l':
            createddate = obj.create_date + datetime.timedelta(hours=8)
            createddate = createddate.strftime('%Y-%m-%d %H:%M:%S')
            self.mself.statusBar().showMessage(str(obj.id) + ' ' + createddate)
        else:
            self.mysender(obj.id)

    def set_mysender(self,mysender):
        self.mysender = mysender

    def set_label_treeitems(self,label_id_set,Mself):

        for i in range(self.topLevelItemCount()):
            sip.delete(self.topLevelItem(0))

        labels = list(MyQuery(label_id_set,Label))
        labels_values = [{
                            'id':label.id,
                            'name':label.name,
                            'pid':label.pid,
                            'queue':label.queue,
                            'grade':label.grade,
                            'create_date':label.create_date,
                        } 
                        for label in MyQuery(label_id_set,Label)]

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

                # item.setExpanded(bool(self.mself.expanddict.get(cobj.id)))

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


            # item.setExpanded(bool(self.mself.expanddict.get(cobj.id)))

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

            for cobj in MyQuery(content_id_set,Content):
                item = TreeWidgetItem(pitem)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
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

    def itemDoubleClicked_connect(self,item,column):
        # sender = self.sender()
        # print(item.text(column))
        # print(11)
        # print(item.text(column))
        # print(item.isExpanded())
        item.setExpanded( item.isExpanded())
        id_ = item.model_data['object'].id
        self.mself.expanddict[id_] = not(item.isExpanded())
        # print(self.mself.expanddict)
    
    def save_queue(self,item):
        print('save_queue',end='\r')
        if not item:
            return
        obj = item.model_data['object']
        if gettype(obj) != 'l':
            return
        queue = [[],[]]
        for citem in self.children(item):
            cobj = citem.model_data['object']
            if gettype(cobj) == 'l':
                queue[0].append(str(cobj.id))
            elif gettype(cobj) == 'c':
                queue[1].append(str(cobj.id))

        queue = (','.join(queue[0]),','.join(queue[1]))
        queue = '|'.join(queue)
        obj.queue = queue
        obj.save()

    def set_content_to_tree_top(self, content_id_set):
        if not content_id_set:
            return 0

        for cobj in MyQuery(content_id_set,Content):
            item = TreeWidgetItem()
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setText(0,cobj.name)
            item.model_data = {
                                'id':cobj.id,
                                'name':cobj.name,
                                'text':cobj.text,
                                'object':cobj,
            }
            item.typelc = 'c'
            self.insertTopLevelItem(0,item)

    # 旧的 --------------------------------------------------
    def setitem(self,labels=None,contents=None):

        for i in range(self.topLevelItemCount()):
            sip.delete(self.topLevelItem(0))

        #-------------------重写formysql-------------------
        if not labels and not contents:
            labels = models.Label.objects.all().order_by('id')
            labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))
        elif not labels:
            labels = []
        else:
            labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))
        #-------------------重写formysql-------------------
        #
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
        # print(111111111)
        self.setcontent(labels,contents)
        # print(222222222)


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




        self.clicked.connect(self.itemClicked_connect)
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

    def itemClicked_connect(self):
        item = self.currentItem()
        if hasattr(item,'model_data'):
            id_ = item.model_data['object'].id
            self.mself.dia_le.setText(str(id_))
        else:
            print('没有 model_data')

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

    def get_Labels(self):

        # 应该是修改好了
        #-------------------重写formysql-------------------
        # labels = models.Label.objects.all().order_by('id')

        labels = list(models.labeldict.values())
        labels.sort()
        labels_values = [ {  j:i   for i,j in zip(label,LABEL_FIELDS)} for label in labels]
        # labels_values = list(labels.values('id','name','pid','queue','grade','create_date'))
        # labels = list(labels)
        # 
        queue_queue = {'data':None,'children':{}}
        queue_child_dict = {1:queue_queue['children']}
        rest = {}
        #-------------------重写formysql-------------------
        
        c = 0
        for i in range(len(labels)):
            la = MyModels(Label,None,labels[i][0])
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
        print('rest 是否可以取消字典改为 set',end='\r')


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

                # item.setExpanded(bool(self.mself.expanddict.get(item.model_data['object'].id)))

        for fchild in queue_queue['children'].values():
            item = TreeWidgetItem(self)
            item.setText(0,fchild['data']['name'])

            # 1 字典 2 model
            item.model_data = fchild['data']
            add_tree_child_item(item,fchild)

            # item.setExpanded(bool(self.mself.expanddict.get(item.model_data['object'].id)))

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
            else:
                queue = []
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
        self.mself.dia_le.setText('%s' % obj.id)

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
        self.mself.dia_le.setText('%s' % obj.id)

        # 修改 parent 排序
        if pid != 1:
            pitem = item.parent()
            lobj = pitem.model_data['object']
            que = QueueDeal(lobj.queue)
            que.queue[0] = [ str(pitem.child(i).model_data['object'].id) for i in range(pitem.childCount())]
            lobj.queue = que.queue2str()
            lobj.save()


class Mainwindow(QMainWindow):

    def __init__(self):
        single_windows(self)
        super().__init__()
        self.is_show_labels_pre = True
        self.show_label_lst = []
        self.expanddict = {}
        self.content_layout_current_id = None


        self.hc = None # HCalendar
        self.le1 = None
        self.tree = None
        self.textEdit = None
        self.cl_bt_le = None
        self.pin = Pinyin()

        self.load_Expanded()



        # 每5分钟保存一次
        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.timer_save) 
        self.timer.start(1000 * 60 * 5)

        self.timer_save_time = None

        # 每30分钟连接服务器一次
        self.timer_connect = QTimer(self)
        self.timer_connect.setSingleShot(False)
        self.timer_connect.timeout.connect(self.connect_db)
        self.timer_connect.start(1000 * 60 * 5)



        MyModels.mself = self

        global models
        models = MyModels()

        self.get_labels_by_content = models.get_labels_by_content
        self.get_contents_by_label = models.get_contents_by_label
        # self.labeldict = MyQuery(models.labeldict,Label)
        # self.contentdict = MyQuery(models.contentdict,Content)

        self.iaa = 1

        t1 = ConnThread(self)
        t1.start()

        self.initUI()
        self.addNewFunc()

    # @tryruntime
    def connect_db(self):
        # x = list(models.Content.objects.filter(id = -100))
        MyModels().time_connect()
        print('每半小时连接一次服务器 成功连接 ',end='\r')

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
        self.textEdit = TextEdit(mself=self)
        self.le1 = QLineEdit()
        self.le1.returnPressed.connect(self.search_models)

        # self.cl_bt_bt = QLabel('标签')
        
        cl_bt_hbox = QHBoxLayout()
        self.cl_bt_le = QLineEdit('内容')
        self.cl_bt_bt = QPushButton('local')
        self.cl_bt_bt.clicked.connect(self.cl_bt_bt_clicked)
        
        if models.local_data and models.mysql_data:
            cl_bt_hbox.addWidget(self.cl_bt_bt)

        # self.cl_bt_le.textChanged.connect(self.cl_bt_le_textChanged)
        cl_bt_hbox.addWidget(self.cl_bt_le)
        # self.content_layout = 





        vbox_left.addWidget(self.le1)
        vbox_left.addWidget(self.tree)
        vbox_right.addWidget(self.textEdit)

        self.hc = HCalendar(self.tree,self.textEdit)

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





        menubar = self.menuBar()
        self.file = menubar.addMenu('&File')

        # set shortcut
        self.set_shortcut('save','Ctrl+S',self.save_text)
        # self.set_shortcut('save_all','Ctrl+Shift+S',self.save_text_all)

        self.set_shortcut('embark','alt+q',self.exec_test)
        self.set_shortcut('embark2','alt+e',self.embark_shortcut )
        self.set_shortcut('writetime','Ctrl+T',self.shortcut_writetime )
        self.set_shortcut('writetime','alt+T',self.shortcut_writetime )
        self.set_shortcut('git','alt+G',self.shortcut_git )
        self.set_shortcut('shotscreen','alt+B',self.shortcut_shotscreen )
        self.set_shortcut('setmm','ctrl+m',self.shortcut_setmm )
        self.set_shortcut('examine_data','ctrl+E',self.shortcut_examine_data )
        self.set_shortcut('copy_text','ctrl+shift+c',self.shortcut_copy_text )



        # 设置 le1的上下文菜单
        self.le1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.le1.customContextMenuRequested.connect(self.showLe1Menu)
        self.labelhistory = LabelHistory()


        self.show()
        self.show_labels()

    def addNewFunc(self):
        pass

    def moveEvent(self,e):
        follow_know_windows(self)

    def closeEvent(self, event):
        if self.shortcut_examine_data():
            super().closeEvent(event)
        else:
            event.ignore()

    def set_shortcut(self,name,shortcut,fun):
        save = QAction(QIcon(''),  name,  self)
        save.setShortcut(shortcut)
        save.setStatusTip(name + ' application')
        save.triggered.connect(fun)

        self.file.addAction(save)

    def save_text(self):
        self.show_labels_pre()
        self.save_Expanded()

        if models.local_data and models.mysql_data:
            local_labelset = models.local_data[2][self.content_layout_current_id]
            mysql_labelset = models.mysql_data[2][self.content_layout_current_id]

            if self.cl_bt_bt.text() == 'mysql':
                models.local_data[2][self.content_layout_current_id] = mysql_labelset

            elif self.cl_bt_bt.text() == 'local':
                adds = local_labelset - mysql_labelset
                dels = mysql_labelset - local_labelset
                cobj = MyModels(Content,None,self.content_layout_current_id)
                for add_ in adds:
                    cobj.labels.add(MyModels(Label,None,add_))
                for del_ in dels:
                    cobj.labels.remove(MyModels(Label,None,del_))

        local_all_data = MyModels().all_data
        save_all_data(*local_all_data)

    def save_Expanded(self):
        filename = os.path.join(CURRENTURL,'expand.dat') 

        for _ in range(3):
            try:
                with open(filename,'wb') as f:
                    pickle.dump(self.expanddict,f)
                break
            except PermissionError:
                time.sleep(2)

    def load_Expanded(self):
        filename = os.path.join(CURRENTURL,'expand.dat') 

        if os.path.isfile(filename):
            with open(filename,'rb') as f:
                self.expanddict = pickle.load(f)

    def embark_shortcut(self):
        # print(11)
        # cobj = models.Content.objects.get(name='know快捷键')
        cobj = MyModels(Content,None,141)
        if cobj.name != 'know快捷键':
            raise ValueError('name is %s not know_setting' % cobj.name)

        res1 = re.findall(r'\<sublime\>([\w\W]+)\<sublimeend\>',cobj.text)[0].strip()
        res1 = [   s.split('|')          for s in res1.split('\n')]
        res1 = dict(res1)

        res2 = re.findall(r'\<python\>([\w\W]+)\<pythonend\>',cobj.text)[0].strip()
        res2 = [   s.split('|')          for s in res2.split('\n')]
        res2 = dict(res2)

        res = (res1,res2)
        return res

    def shortcut_writetime(self):
        # print(111)
        time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
        week = datetime.datetime.now().weekday() + 1
        time_now_str = time_now_str[:8] + '-%d' % week + time_now_str[8:]
        self.textEdit.insertPlainText(time_now_str)

    def shortcut_git(self):
        # return myexec()

        # locale.setlocale(locale.LC_ALL,'zh_CN.UTF-8')

        # cmd = 'mkdir 11xxzz'

        x = list(set(self.textEdit.git_pathdict))
        x.append('all')
        x = ' '.join(x)
        x = x + '\n' + self.textEdit.git_cwd
 
        self.content_layout_current_id = None

        # x = os.getcwd()
        self.cl_bt_le.setText('<git>')
        self.textEdit.setText(x)

        
        cursor = self.textEdit.textCursor()
        self.textEdit.moveCursor(cursor.End,cursor.MoveAnchor)

    def shortcut_shotscreen(self):
        # app = QApplication.instance() or QApplication(sys.argv)
        screen_capture.WScreenShot.run()
        # app.exec_()

    def shortcut_setmm(self):
        id_ = self.content_layout_current_id
        self.label_tree_clicked(1236)
        self.textEdit.ctrl_M()
        self.label_tree_clicked(id_)

    def shortcut_examine_data(self):
        models = MyModels()
        local_all_data = models.all_data
        save_all_data(*local_all_data)
        return models.check_data()

    def shortcut_copy_text(self):
        text = (models.contentdict[170][2])
        text = re.findall(r'<copy_texts>([\w\W]*?)<copy_texte>',text)[0]
        text = text.split('\n')[1].strip()
        pyperclip.copy(text)

    def exec_test(self):
        # return myexec()
        self.connect_db()

    def show_labels_pre(self):
        
        self.timer_save_time = time.time()
        '保存textedit的数据'
        if not self.is_show_labels_pre:
            return

        if self.content_layout_current_id:
            # obj = models.Content.objects.get(id = self.content_layout_current_id)
            obj = MyModels(Content,None,self.content_layout_current_id)

            name = self.cl_bt_le.text()

            # 应该是为了删除图片的残留
            text = self.textEdit.toPlainText().replace('\ufffc','')
            change = False
            if name != obj.name:
                change = True
                obj.name = name
                for item in self.tree.content_item_dict[obj.id]:
                    try:
                        item.setText(0,name)
                    except RuntimeError:
                        # print('RuntimeError again')
                        pass
            # 进行加密
            text = self.textEdit.mmcrypto.mEncrypt(text)

            # 反引用
            text = self.textEdit.quote_recovery(text)

            if text != obj.text:
                change = True
                obj.text = text

            if change:

                obj.save()
                print('数据保存完成',end='\r')

    def show_labels(self):
        '设置 textedit 和 cl_bt_le 的文字 并生成标签'
        # return myexec()
        for bt in self.show_label_lst:
            sip.delete(bt)
        self.show_label_lst = []

        if self.content_layout_current_id:
            obj = MyModels(Content,None,self.content_layout_current_id) #        models.Content.objects.get(id = self.content_layout_current_id)
            self.cl_bt_le.setText(obj.name)
            letextlst = self.le1.text().split()
            text = obj.text

            # 解密
            text = self.textEdit.mmcrypto.mDecrypt(text)

            # 引用
            text = self.textEdit.quote_read(text)

            self.textEdit.setText(text)

            # 读取服务器上的数据
            if self.content_layout_current_id == 395:
                self.textEdit.setText(obj.get_content395())
            
            # 设置数据
            self.set_textEdit()

            createddate = obj.create_date + datetime.timedelta(hours=8)
            createddate = createddate.strftime('%Y-%m-%d %H:%M:%S')

            rest_seconds = self.hc.show_by_seconds(obj)
            if rest_seconds:
                self.statusBar().showMessage(str(obj.id) + ' ' + createddate + ' ' + (str(rest_seconds) if rest_seconds else ''))
            else:
                self.statusBar().showMessage(str(obj.id) + ' ' + createddate)



            labs = MyQuery(models.all_data[2].get(obj.id,{}),Label) #        obj.labels.all()
            # strr = labs.values('name')
            # strr = [ s['name'] for s in strr]
            labs = list(labs)
            # pprint(models.all_data[2].get(obj.id,{}))
            strr = [la.name for la in labs]

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
        
        bttemp = QPushButton('新建')
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
                bt.setzself(self)
                # bt.isnew = True
                layout.addWidget(bt)
                self.show_label_lst.append(bt)

            self.show_label_lst.append(layout)
            layout.addStretch()

    def set_textEdit(self):

        # 设置字体颜色
        letextlst = self.le1.text().split()
        x = self.textEdit.textCursor()
        self.textEdit.moveCursor(x.Start,x.MoveAnchor)
        self.textEdit.moveCursor(x.End,x.KeepAnchor)
        find_cursor = self.textEdit.textCursor()
        plainFormat = QTextCharFormat(find_cursor.charFormat())
        colorFormat = plainFormat
        colorFormat.setForeground(Qt.black)
        self.textEdit.mergeCurrentCharFormat(colorFormat)

        for to_find_text in letextlst:
            to_find_text = to_find_text.lstrip('~')
            x = self.textEdit.textCursor()
            self.textEdit.moveCursor(x.Start,x.MoveAnchor)

            while self.textEdit.find(to_find_text):
                find_cursor = self.textEdit.textCursor()
                plainFormat = QTextCharFormat(find_cursor.charFormat())
                colorFormat = plainFormat
                colorFormat.setForeground(Qt.red)
                self.textEdit.mergeCurrentCharFormat(colorFormat)

        # 设置图片
        x = self.textEdit.textCursor()
        self.textEdit.moveCursor(x.Start,x.MoveAnchor)

        while self.textEdit.find(QRegExp('<hgpic=\\d+>')):

            id_ = self.textEdit.textCursor().selectedText()
            id_ = re.findall('<hgpic=(\\d+)>',id_)[0]
            fname = os.path.join(CURRENTURL,'kqj','data','static','pic',id_)
            fragment = QTextDocumentFragment.fromHtml("<img src='%s'>" % fname)

            self.textEdit.moveCursor(x.Left,x.MoveAnchor)
            self.textEdit.textCursor().insertFragment(fragment);
            self.textEdit.find(QRegExp('<hgpic=\\d+>'))
        self.textEdit.moveCursor(x.Start,x.MoveAnchor)

    def cl_bt_bt_clicked(self):
        # return myexec()
        self.is_show_labels_pre = False
        # print(len(models.local_data[0]))
        if models.local_data and models.mysql_data:
            if self.cl_bt_bt.text() == 'mysql':
                self.cl_bt_bt.setText('local')
                models.all_data[0] = models.local_data[0]
                models.all_data[1] = models.local_data[1]
                models.all_data[2] = models.local_data[2]
                models.all_data[3] = models.local_data[3]
            elif self.cl_bt_bt.text() == 'local':
                self.cl_bt_bt.setText('mysql')

                models.all_data[0] = models.mysql_data[0]
                models.all_data[1] = models.mysql_data[1]
                models.all_data[2] = models.mysql_data[2]
                models.all_data[3] = models.mysql_data[3]
            self.tree.mysender(self.content_layout_current_id)


        self.is_show_labels_pre = True
        # item = TreeWidgetItem(self.tree)
        # item.setText(0,cobj.name)
        # item.model_data = {
        #                     'id':cobj.id,
        #                     'name':cobj.name,
        #                     'text':cobj.text,
        #                     'object':cobj,
        # }

    def addlabel(self):

        self.show_labels_pre()

        self.bt_sender = self.sender()
        
        self.dia = QDialog(self)
        vbox = QVBoxLayout()
        self.dia.setLayout(vbox)
        self.ltree = LabelTree()

        self.ltree.set_mself(self)

        self.dia_le = QLineEdit('126')

        ok_bt = QPushButton('确定')
        ok_bt.clicked.connect(self.dia_ok_bt_clicked)

        cancel_bt = QPushButton('取消')
        cancel_bt.clicked.connect(self.dia_cancel_bt_clicked)

        hbox = QHBoxLayout()
        vbox.addWidget(self.ltree)
        hbox.addWidget(self.dia_le)
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
        # return myexec()
        obj = MyModels(Content,None,self.content_layout_current_id)

        objlabelset = models.all_data[2].get(obj.id,None)
        changedlabelset = []

        add_label_id = None
        del_label_id = None

        if self.bt_sender.model_data:
            # print(self.bt_sender.model_data['object'])
            # print(type(self.bt_sender.model_data['object']))
            objlabelset.remove(self.bt_sender.model_data['object'].id)
            del_label_id = self.bt_sender.model_data['object'].id
            obj.labels.remove(self.bt_sender.model_data['object'])


        # lobj = self.ltree.get_currentItem_model_data()['object']
        lobj = MyModels(Label,None,int(self.dia_le.text()))
        # objlabelset = set(objlabelset)
        if not objlabelset:
            objlabelset = {lobj.id}
        else:
            objlabelset.add(lobj.id)
        
        if del_label_id == lobj.id:
            del_label_id = None
        else:
            add_label_id = lobj.id

        obj.labels.add(lobj)

        # print(objlabelset)
        models.all_data[2][obj.id] = objlabelset
        # 修改label content置顶
        que = QueueDeal(lobj.queue)
        id_ = str(obj.id)
        if id_ in que.queue[1]:
            que.queue[1].remove(id_)
        que.queue[1].insert(0,id_)
        lobj.queue = que.queue2str()
        lobj.save()


        # 根据修改的label移动content
        self.contentmove(obj.id,add_label_id,del_label_id)

        # self.get_contents_by_label = {}
        # self.labeldict = {}
        # self.contentdict = {}

        # 设置lobj的排序
        self.show_labels()
        self.search_models()
        self.dia.close()

    def dia_cancel_bt_clicked(self):
        # obj = models.Content.objects.get(id=)
        obj = MyModels(Content,None,self.content_layout_current_id)
        if self.bt_sender.model_data:



            button=QMessageBox.question(self,"Question",  
                                               self.tr("是否确认删除?"),  
                                               QMessageBox.Ok|QMessageBox.Cancel,  
                                               QMessageBox.Ok)  
            if button==QMessageBox.Ok:  
                obj.labels.remove(self.bt_sender.model_data['object'])
                self.show_labels()
                del_label_id = self.bt_sender.model_data['object'].id
                self.contentmove(obj.id,-1,del_label_id)
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

    def contentmove(self,objid,add_label_id,del_label_id,pitem = None):
        if not add_label_id and not del_label_id:
            return
        for item in self.tree.children(pitem):
            lobj = item.model_data['object']
            if gettype(lobj) == 'l':
                self.contentmove(objid,add_label_id,del_label_id,item)

                if del_label_id == lobj.id:
                    for c in self.tree.children(item):
                        co = c.model_data['object']
                        if gettype(co) == 'c' and co.id == objid:
                            sip.delete(c)

                elif add_label_id == lobj.id:

                    hascontent = True

                    for c in self.tree.children(item):
                        co = c.model_data['object']
                        if gettype(co) == 'c' and co.id == objid:
                            break
                    else:
                        hascontent = False

                    if not hascontent:
                        citem = TreeWidgetItem()
                        cobj = MyModels(Content,None,objid)
                        citem.setText(0,cobj.name)
                        citem.model_data = {
                                            'id':cobj.id,
                                            'name':cobj.name,
                                            'text':cobj.text,
                                            'object':cobj,
                        }
                        font = QFont()
                        font.setBold(True)
                        citem.setFont(0,font)
                        self.tree.insertItem(item,0,citem)

    def label_tree_clicked(self,id):

        self.show_labels_pre()
        self.content_layout_current_id = id
        self.show_labels()

    def search_models(self):
        text = self.le1.text()
        self.labelhistory.addHistory(text)

        if text[0] == '#':
            # cobj = models.Content.objects.get(name='know_setting')
            cobj = MyModels(Content,None,170)
            if cobj.name != 'know_setting':
                raise ValueError('name is %s not know_setting' % cobj.name)
            
            res = re.findall(r'\<knowset\>([\w\W]+)\<knowsetend\>',cobj.text)[0].strip()
            res = [   s.split(' ')          for s in res.split('\n')]
            res = dict(res)
            res = res.get(text[1:])
            
            if res:
                # cobjtemp = models.Content.objects.get(id=res)
                try:
                    res = int(res)
                    # models.Content.objects.get(id=res)
                    self.label_tree_clicked(res)
                    return None

                except models.Content.DoesNotExist:
                    print('错误的content id',res)
            
        elif text[0] == '@':
            cobj = MyModels(Content,None,170)
            if cobj.name != 'know_setting':
                raise ValueError('name is %s not know_setting' % cobj.name)

            res = re.findall(r'\<knowlabelname\>([\w\W]+)\<knowlabelnameend\>',cobj.text)[0].strip()
            res = [   s.split(' ')          for s in res.split('\n')]
            res = dict(res)
            res = res.get(text[1:])
            if res:
                self.le1.setText(res)

        elif text[0] in '!！' :
            res = text[1:].strip().split()[0]
            if res.isdigit():
                try:
                    res = int(res)
                    self.label_tree_clicked(res)
                    return None
                except models.Content.DoesNotExist:
                    print('错误的content id',res)
        elif text[0] == '~':
            res = text[1:].strip().split()[0]
            know002_search_again(self,res)
            return None


        def get_contents_by_textlst(textlst):

            def get_label_children(label_id_set):
                llen = len(label_id_set)
                for label in MyQuery(models.labeldict,Label):
                    # label = self.labeldict[i]
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
                for label in MyQuery(models.labeldict,Label):
                    # label = self.labeldict[i]
                    if text.lower() in label.name.lower() or text.lower() in self.pin.get_pinyin(label.name,''):
                        label_id_set.add(label.id)


                get_label_children(label_id_set)

                # pprint(label_id_set)

                # for id_ in label_id_set:
                #     content_id_set_by_label |= self.get_contents_by_label.get(id_,set())

                for content in MyQuery(models.contentdict,Content):
                    id_ = content.id
                    if text.lower() in content.name.lower() or text.lower() in self.pin.get_pinyin(content.name,''):
                        content_id_set_by_text.add(id_)
                    elif text.lower() in content.text.lower():
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



        # 不需要了
        # def set_all_data():
        #     self.get_labels_by_content = {}
        #     self.get_contents_by_label = {}
        #     self.labeldict = {}
        #     self.contentdict = {}


        #     def set_content_labels():
        #         cursor = connection.cursor()
        #         sql = 'select content_id,label_id from data_content_labels;'
        #         cursor.execute(sql)
        #         rows = cursor.fetchall()

        #         for row in rows:
        #             labels_set = self.get_labels_by_content.get(row[0])
        #             if not labels_set:
        #                 self.get_labels_by_content[row[0]] = {row[1]}
        #             else:
        #                 labels_set.add(row[1])

        #             contents_set = self.get_contents_by_label.get(row[1])
        #             if not contents_set:
        #                 self.get_contents_by_label[row[1]] = {row[0]}
        #             else:
        #                 contents_set.add(row[0])

        #     labelall = models.Label.objects.all()
        #     contentall = models.Content.objects.all()
            

        #     for label in labelall:
        #         self.labeldict[label.id] = label
            

        #     for content in contentall:
        #         self.contentdict[content.id] = content

            
        #     set_content_labels()

        # set_all_data()



        textlst = self.le1.text().split(' ')
        # pprint(self.get_contents_by_label)
        content_id_set_by_text,label_id_set = get_contents_by_textlst(textlst)
        # label_id_set = get_labels_by_content_id_set(content_id_set_by_label)

        self.tree.set_label_treeitems(label_id_set,self)
        self.tree.setcontent(label_id_set,content_id_set_by_text,self)
        self.tree.h_sort()

        self.hc.h_sort_by_tree(self.tree)
        # self.tree.setcontent(set(),content_id_set_by_true_text,self,False)

    def showLe1Menu(self, pos):
        strlst = self.labelhistory.getSort()
        self.contextMenu = QMenu(self)

        for s in strlst:
            t = self.contextMenu.addAction(s)
            t.triggered.connect(self.pushLe1Menu)

        self.contextMenu.exec_(QCursor.pos()) #在鼠标位置显示

    def pushLe1Menu(self):
        self.le1.setText(self.sender().text())
        self.search_models()

    def timer_save(self):
        if not self.timer_save_time:
            self.timer_save_time = time.time()
            return
        now = time.time()
        if now - self.timer_save_time > 60 * 10:
            self.show_labels_pre()
            print(time.ctime(),'完成备份' , end = '\r')

    # 旧的
    def search_models_none(self):
        def labels_children(labels):
            ls = set()
            for l in labels:
                ls |= set([l.id for l in models.Label.objects.filter(pid=l)])
            return labels | labels_children(ls) if ls else labels

        text = self.le1.text()

        # objsall = models.Content.objects.filter(id=-1111)
        cidset = set()
        if not text:
            labelobjs = None
        else:
            for te in text.split(' '):
                #-------------------重写formysql-------------------






                cobjs = models.Content.objects.filter(Q(name__contains=te) | Q(text__contains=te) ) #| Q(labels__name__contains=te)






                labels = models.Label.objects.filter(name__contains=te)

                labels = labels_children(set([l.id for l in labels]))
                # cobjs |= models.Content.objects.filter(labels__id__in=labels)
                
                labelobjs = models.Label.objects.filter(id__in=labels)
                #-------------------重写formysql-------------------
                # if objsall:
                #     objsall = objsall & cobjs
                # else:
                #     objsall = cobjs
            cidset = models.filter_cid_by_textlst(te)

        self.tree.setitem(labelobjs,cidset) #labelobjs

class QueueDeal(object):
    """docstring for QueueDeal"""
    def __init__(self, queue):
        self.queue = queue
        self.set_tqueue()

    def set_tqueue(self):
        if not self.queue:
            self.queue = [[],[]]
            return
        self.queue = self.queue.split('|')
        self.queue = [      q.split(',') if q else []    for q in self.queue]

    def queue2str(self):
        queue = self.queue
        queue = [ ','.join(q) if q else '' for q in queue ]
        if queue and len(queue) == 2:
            return '|'.join(queue)
        return '|'
        


if __name__ == '__main__':
    obj = models.Content
    print(obj)

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

