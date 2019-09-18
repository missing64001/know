

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