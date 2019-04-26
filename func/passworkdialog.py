#coding=utf-8
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit)
import sys


class PasswdDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(200,100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：",self)

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)

        self.bt1 = QPushButton("确定",self)
        self.bt2 = QPushButton("取消",self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        """
        这个三个语句是给密码输入框增加一些属性
        """
        self.edit.setContextMenuPolicy(Qt.NoContextMenu)#这个语句设置QLineEdit对象的上下文菜单的策略。复制，粘贴，。。。，是否可用
        # self.edit.setPlaceholderText("密码不超15位，只能有数字和字母，必须以字母开头")#只要行编辑为空，设置此属性将使行编辑显示为灰色的占位符文本。默认情况下，此属性包含一个空字符串。这是非常好的使用方法，可以在用户输入密码前看到一些小提示信息，但是又不影响使用，非常棒这个方法。
        self.edit.setEchoMode(QLineEdit.Password)#这条语句设置了如何限定输入框中显示其包含信息的方式，这里设置的是：密码方式，即输入的时候呈现出原点出来。
        

        """
        这三段代码大体意思就是说，运用正则表达式限定密码输入框字符接收的条件：
        长度不能超过15位；
        字母开头；
        后面跟着的字符只能是字母或者数字。
        """
        # regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")#为给定的模式字符串构造一个正则表达式对象。
        # validator = QRegExpValidator(regx, self.edit)#构造一个验证器，该父对象接受与正则表达式匹配的所有字符串。这里的父对象就是QLineEdit对象了。匹配是针对整个字符串; 例如：如果正则表达式是[A-Fa-f0-9]+将被视为^[A-Fa-f0-9]+$。
        # self.edit.setValidator(validator)#将密码输入框设置为仅接受符合验证器条件的输入。 这允许您对可能输入的文本设置任何约束条件。因此我们这里设置的就是符合上面描述的三种约束条件。

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)

        object = QObject()

        """
        事件过滤器可是一个非常重要的概念。根据Qt的官方文档，如果对象被安装已监视对象的事件过滤器，则过滤事件。如果要过滤事件，需重新实现此函数时，若停止进一步处理，返回true； 否则返回false。
        如果一个对象安装多个事件过滤器，那么，最后安装的过滤器首先被激活。    
        """    
    def eventFilter(self, object, event):
        if object == self.edit:#这里是对事件的判断。其中QKeyEvent类描述了一个关键事件。当按下或释放按键时，主要事件将发送到具有键盘输入焦点的小部件。然后运用matches方法匹配具体的按键。
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):#然后进行事件判断与转换：鼠标移动对应的事件类型为QEvent.MouseMove，鼠标双击对应的事件类型为QEvent.MouseButtonDblClick，全选、复制、粘贴对应的事件类型为 QEvent.KeyPress，当接收到这些事件时，需要被过滤掉，所以返回true。
                    return True
        return QDialog.eventFilter(self, object, event)#继续传递该事件到被观察者，由其本身调用相应的事件

    def Ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        # elif len(self.text) < 6:
        #     QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            self.done(1)          # 结束对话框返回1

    def Cancel(self):
        self.done(0)          # 结束对话框返回0




class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(380,180)
        self.setWindowTitle('早点毕业吧--自定义密码输入对话框')

        self.lb1 = QLabel('密码在此显示...',self)
        self.lb1.move(20,20)


        self.bt1 = QPushButton('输入密码(普通型)',self)
        self.bt1.move(20,60)

        self.bt2 = QPushButton('输入密码(普通加强型)',self)
        self.bt2.move(20,100)

        self.bt3 = QPushButton('输入密码(特别加强型)',self)
        self.bt3.move(20,140)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：',QLineEdit.Password)
            if ok:
                self.lb1.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '密码输入框', '请输入密码：',QLineEdit.PasswordEchoOnEdit)
            if ok:
                self.lb1.setText(text)
        else:
            pwd = PasswdDialog()
            r = pwd.exec_()
            if r:
                self.lb1.setText(pwd.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
