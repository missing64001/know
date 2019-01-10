
# _*_ coding:UTF-8 _*_  
import win32con
import ctypes
import ctypes.wintypes
from PyQt5.QtCore import QThread

user32 = ctypes.windll.user32  #加载user32.dll
id1=105 #注册热键的唯一id，用来区分热键
id2=106

class Hotkey(QThread):  #创建一个Thread.QThread的扩展类  
    def __init__(self,fun, parent=None):
        self.fun = fun
        super().__init__(parent)

    def run(self):  
        global EXIT  #定义全局变量，这个可以在不同线程间共用。
        global RUN  #定义全局变量，这个可以在不同线程间共用。

        if not user32.RegisterHotKey(None, id1, 0, 65):   # 注册快捷键F9并判断是否成功，该热键用于执行一次需要执行的内容。  
            print ("Unable to register id", id1) # 返回一个错误信息

        if not user32.RegisterHotKey(None, id2, win32con.MOD_ALT, 66):   # 注册快捷键F10并判断是否成功，该热键用于结束程序，且最好这么结束，否则影响下一次注册热键。  
            print ("Unable to register id", id2)

        #以下为检测热键是否被按下，并在最后释放快捷键  
        try:  
            msg = ctypes.wintypes.MSG()  

            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:

                    if msg.message == win32con.WM_HOTKEY:  
                        if msg.wParam == id1:

                            RUN = True
                            self.fun()
                        elif msg.wParam == id2:

                            exit()

                    user32.TranslateMessage(ctypes.byref(msg))  
                    user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            user32.UnregisterHotKey(None, id1)#必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
                                              #那么下次很可能就没办法注册成功了，这时可以换一个热键测试
            user32.UnregisterHotKey(None, id2)


def fun1():
    print('zzz')


hotkey = Hotkey(fun1)  
hotkey.start()  