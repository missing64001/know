# import myfn
# print(myfn.get_computer_info)
# self.statusBar().showMessage('Reday')


# import datetime

# obj = models.Content.objects.get(id = 126)
# createddate = obj.create_date + datetime.timedelta(hours=8)
# print(obj.create_date)
# print(createddate.strftime('%Y-%m-%d %H:%M:%S'))



# TextEdit().insertPlainText('122222222222221')

# time_now_str = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
# self.textEdit.insertPlainText(time_now_str)
# pprint(dir())





# self.set_shortcut('embark2','ctrl+e',self.exec_test )

# import win32api
# import win32con

# # win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
# # win32api.keybd_event(86,0,0,0)  #v键位码是86
# # win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
# # win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
# print(ord('下'))

# str_ = '20181130T10:45:46'
# for s in str_:
#     s = ord(s)
#     print(s,chr(s))
#     win32api.keybd_event(s,0,0,0)  #v键位码是86
#     win32api.keybd_event(s,0,win32con.KEYEVENTF_KEYUP,0) #释放按键

# x = self.textEdit.find('eva')
# print(x)

# find_cursor = self.textEdit.textCursor()
# plainFormat = QTextCharFormat(find_cursor.charFormat())
# colorFormat = plainFormat
# colorFormat.setForeground(Qt.red)
# self.textEdit.mergeCurrentCharFormat(colorFormat)



# self.moveCursor(x.EndOfLine,x.KeepAnchor)

# 
# 
# 



print(111)

sitems = self.selectedItems()
        
for item in sitems:
    pitem = item.parent()
    item.oldparent = (pitem, self.indexItem(item), item)

QTreeWidget.dropEvent(self,event)


for item in sitems:
    obj = item.model_data['object']
    pobj = item.parent().model_data['object']
    oldpobj = item.oldparent[0].model_data['object']
    if not item.parent() or not isinstance(pobj, models.Label):
        pitem = item.parent()
        self.removeItem(pitem,item)
        self.insertItem(*item.oldparent)
    elif isinstance(obj, models.Content):
        if oldpobj != pobj:
            print('budeng')
            obj.labels.remove(oldpobj)
            obj.labels.add(pobj)
            obj.save()