from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
'''
# Qt 中无法导入 QScreen 类
try:
    from PySide2.QtGui import QScreen
except:
    from PyQt5.QtGui import QScreen
'''
import sys


class WScreenShot(QWidget):
    
    win = ''
    
    @classmethod
    def run(cls):
        cls.win = cls()
        cls.win.show()
    
    def __init__(self, parent = None):
        super(WScreenShot, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        # desktop = QApplication.desktop()
        # rect = desktop.availableGeometry()
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        if self.isDrawing:  
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen) 
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True
        
    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # PySide2
            #screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
            # PyQt5
            #screenshot = QApplication.primaryScreen().grabWindow(0)
            # 通用
            screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
            
            x1 = min(self.startPoint.x(),self.endPoint.x())
            y1 = min(self.startPoint.y(),self.endPoint.y())
            x2 = max(self.startPoint.x(),self.endPoint.x()) - x1
            y2 = max(self.startPoint.y(),self.endPoint.y()) - y1
            rect = QRect(x1,y1,x2,y2)
            # rect = QRect(abs(rect.x()),abs(rect.y()),abs(rect.width()),abs(rect.height()))
            # print(self.startPoint)
            # print(self.endPoint)
            # from pprint import pprint
            # print(rect)
            outputRegion = screenshot.copy(rect)

            QGuiApplication.clipboard().setPixmap(outputRegion)
            self.close()

if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)
    WScreenShot.run()
    app.exec_()