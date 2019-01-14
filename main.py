import sys
import os
from PyQt5.QtWidgets import QApplication
from qt import Mainwindow
from hmysql import models
import traceback
import time
from PyQt5.QtCore import QThread

def main():
    try:
        app = QApplication(sys.argv)
        ex = Mainwindow()
        # print(models.Label.objects.all().count())
        # print(models.Content.objects.all().count())
        sys.exit(app.exec_())
    except Exception:
        time.sleep(3)
        traceback.print_exc()
        # main()
    finally:
        print('备份了数据')
        os.system(r'F:\my\package\mysqldump.exe -h120.79.41.9 -uknow -pknow know  > F:\my\P028_knowledge_system\knowqt\baksql\%d.sql' % int(time.time()))







if __name__ == '__main__':
    main()
    # a = ['1']
    # b = ','.join(a)
    # print(b)





    # models.Label.objects.create(name='main',pid=-1,queue='',grade=10)
    # models.Label.objects.create(name='22',pid=9,queue='',grade=10)
    # models.Label.objects.create(name='33',pid=3,queue='',grade=10)
    # models.Label.objects.create(name='44',pid=4,queue='',grade=10)
    # models.Label.objects.create(name='55',pid=1,queue='',grade=10)

    # lbs = models.Label.objects.all()
    # models.Content.objects.create(name='yy',text='yyyy').labels.add(lbs[4],lbs[5])
    # models.Content.objects.create(name='xzzx',text='zz').labels.add(lbs[3],lbs[7])
    # models.Content.objects.create(name='zz',text='sdfd').labels.add(lbs[8],lbs[9])




