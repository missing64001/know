

from qt import TextEdit
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys





class QQ(QMainWindow):
    def closeEvent(self, event):
        print(111)
        event.ignore()




app = QApplication(sys.argv)
ex = QQ()
ex.show()
sys.exit(app.exec_())