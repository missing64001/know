import sys
import os
from PyQt5.QtWidgets import QApplication
from qt import Mainwindow
from hmysql import models,MyModels,get_md5,get_all_data_from_mysql,get_all_data_from_local,ALLDATA_FILENAME,save_all_data
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
        # print('备份了数据')
        # os.system(r'F:\my\package\mysqldump.exe -h120.79.41.9 -uknow -pknow know  > F:\my\P028_knowledge_system\knowqt\baksql\%d.sql' % int(time.time()))
        return
        local_all_data = MyModels().all_data
        mysql_all_data = get_all_data_from_mysql()

        md5_1 = get_md5(local_all_data)
        md5_2 = get_md5(mysql_all_data)
        if md5_1 == md5_2:
            print('数据一致性验证完成')
        else:
            print('数据不一致保存到了', save_all_data(*mysql_all_data,True))
        save_all_data(*local_all_data)
        print('保存完成')
        # print(md5_2)





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




