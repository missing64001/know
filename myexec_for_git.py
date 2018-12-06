print(111)
import subprocess
# locale.setlocale(locale.LC_ALL,'zh_CN.UTF-8')



cmd = 'git log'
cmd = 'mkdir 11xxzz'

os.chdir(r'F:\my\P028_knowledge_system\knowqt')


with subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as f:
    data = f.stdout.read().decode('utf-8')
x = self.textEdit.toPlainText() 
print(x)
x += data



x = os.getcwd()
self.textEdit.setText(x)
