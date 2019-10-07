from pprint import pprint





from PyQt5.QtWidgets import QWidget,QApplication,QToolTip,QTextEdit,QTreeWidget
import sys

print(dir(QTextEdit))
class Winform(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    winform = Winform()
    winform.show()
    sys.exit(app.exec_())



exit()





# 气泡 显示
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QToolTip,QTextEdit,QTreeWidgetItem
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Winform(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(200,300,400,400)
        self.setWindowTitle("气泡提示<b>demo</b>")

        self.set_subtextedit()


    def initUI(self):
        # QToolTip.setFont(QFont('SansSerif',10))  #提示信息的字体与字号大小
        self.setToolTip("这是一个<b>气泡提示</b>")




    def set_subtextedit(self):
        self.subtextedit = QTextEdit("气泡提示<b>demo</b>")
        self.subtextedit.setWindowFlags(Qt.FramelessWindowHint)
        self.subtextedit.setReadOnly(True)
        self.subtextedit.setWindowOpacity(0.7)
        self.subtextedit.setAlignment(Qt.AlignCenter)
        self.subtextedit.resize(300,30)


        self.subtextedit2 = QTextEdit("气泡提示<b>demo</b>")
        self.subtextedit2.setWindowFlags(Qt.FramelessWindowHint)
        self.subtextedit2.setReadOnly(True)
        self.subtextedit2.setWindowOpacity(0.7)
        self.subtextedit2.resize(300,300)

        self.subtextedit.show()
        self.subtextedit2.show()
        self.subtextedit.close()
        self.subtextedit2.close()
    
    '''重载一下鼠标按下事件(单击)'''
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and QApplication.keyboardModifiers()==Qt.ControlModifier:
            pos = self.mapToGlobal(event.pos())
            posx = pos.x()+20
            posy = pos.y()+20
            self.subtextedit.move(posx,posy)
            self.subtextedit.show()

            self.subtextedit2.move(posx,posy+29)
            self.subtextedit2.show()
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button () == QtCore.Qt.LeftButton:
            self.subtextedit.close()
            self.subtextedit2.close()
        else:
            super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    winform = Winform()
    winform.show()
    sys.exit(app.exec_())


exit()
import imp as impp
import sys

funstr = 'test.test'


funstr = funstr.split('.')
package = funstr[:-1]
funstr = funstr[-1]
imp = __import__('func.hotswap.' + '.'.join(package))
imp = getattr(imp,'hotswap')
for pp in package:
    imp = getattr(imp,pp)
impp.reload(imp)
fun = getattr(imp,funstr)
fun()

# imp.self = self

exit()










# 测试 MyLineEdit
from qt import MyLineEdit
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
ex = MyLineEdit()
ex.show()
sys.exit(app.exec_())

exit()

# 测试热键
funstr = 'cbtx_trans.trans'

funstr = funstr.split('.')
package = funstr[:-1]
funstr = funstr[-1]

imp = __import__('func.hotswap.' + '.'.join(package))
imp = getattr(imp,'hotswap')
for pp in package:
    imp = getattr(imp,pp)
fun = getattr(imp,funstr)

print(fun)








import datetime
import time
time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
week = datetime.datetime.now().weekday() + 1
time_now_str = time_now_str[:8] + '-%d' % week + time_now_str[8:]
print(time_now_str)
exit()


from qt import TextEdit
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys





class QQ(QMainWindow):
    def closeEvent(self, event):
        print(111)
        event.ignore()




app = QApplication(sys.argv)
ex = TextEdit()
ex.show()
sys.exit(app.exec_())



exit()


import os
import sys


res = ['python',r'F:\my\P040_exchange_api\synchro_upload_and_check.py']
if res[0] == 'python':

    exeFile = "C:\\Windows\\System32\\cmd"
    old_path = r'F:\my\P028_knowledge_system\knowqt'
    # exeFile = 'F:\\my\\P028_knowledge_system\\knowqt\\main.py'
    exePath = "F:\\my\\P028_knowledge_system\\knowqt\\"

    file_name = res[1]
    os.chdir(os.path.dirname(file_name))
    os.startfile(res[1],'open')
    # os.system('start /b '+ exeFile)
    os.chdir(old_path)

    if len(res)>2:
        pyperclip.copy(res[2])
        print(res[2][:-1])
    if len(res)>3 and res[3]=='g':
        pyperclip.copy(res[2]+'\r\n')
        print(3)

print(os.getpid())

input('111')