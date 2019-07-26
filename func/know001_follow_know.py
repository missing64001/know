
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import os
import sys

try:
    from gl.gl import reset_window_pos, set_title, myexec
except ImportError:
    CURRENTURL = os.path.dirname(__file__)
    sys.path.insert(1,os.path.dirname(CURRENTURL))
    from gl.gl import reset_window_pos, set_title, myexec
    

def single_windows(self,title='know - 0.9.5'):
    N = reset_window_pos(title)
    if N:
        print('已经开启了 %s' % title)
        exit()
    set_title(title)
    self.hghwnd = reset_window_pos(title)

def follow_know_windows(self):
    geo = self.frameGeometry()
    reset_window_pos('',geo.left(),geo.top()-150,geo.width(),155,self.hghwnd)

class TMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        single_windows(self,'sdggsd')

    def moveEvent(self,e):
        follow_know_windows(self)

    def mouseReleaseEvent(self, event):
        print(3333)

    def releaseMouse(self, event):
        print(444)





if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    TM = TMainWindow()
    TM.show()
    sys.exit(app.exec_())

pos = '''
class Mainwindow(QMainWindow):

    def __init__(self):
        single_windows(self)


    def moveEvent(self,e):
        follow_know_windows(self)

'''