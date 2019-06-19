from qt import TextEdit
from PyQt5.QtWidgets import QApplication
import sys










app = QApplication(sys.argv)
ex = TextEdit()
ex.show()
sys.exit(app.exec_())