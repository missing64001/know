	







import sys
import Timed_restart
from Timed_restart import Timed_restart
import re,os

import time

import urllib.request as http
import time, threading

CURRENTURL = os.path.dirname(__file__)


def str_replace(x,list_str):
	for strr in list_str:
		x = x.replace(strr,"")
	return x
#
def while_run(xx):
	try:
		while 1:
			xx()
	except ZeroDivisionError as e:
	    print('except:', e)
		
	finally:
		print("重新启动")
		# time.sleep(5)
		while_run(xx)




class xiaoshuo(object):
	def __init__(self,url,filename,name):
		self.url = url
		self.filename = filename
		self.name = name
		self.save_mulu()


		# l_day = []
		# rootdir = self.filename
		# for parent,dirnames,filenames in os.walk(rootdir):
		# 	for file in filenames:
		# 		if file[-4:]== ".txt":
		# 			l_day.append(file)
		# 	break
		# i = len(l_day)






class run_class(object):
	def __init__(self):
		self.Timed_restart_time = time.localtime(time.time())
		

	def run(self):
		time_now_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		self.Timed_restart_time = time.localtime(time.time())
		self.threading_lst = {}
		self.hg_head = None
		self.id = -1
		self.is_good_run = True
		sys.stdout.write(time_now_str)
		sys.stdout.write("                                                   \r")
		sys.stdout.flush()
		
		dd = [
		      ["http://www.23wxx.com/9_9064/","jl"], #剑来
		      ["http://www.23wxx.com/9_9398/","ddct"], #侠行天下
		      ["http://www.23wxx.com/9_9096/","nddbz"], #脑洞大爆炸
		      ["http://www.23wxx.com/0_668/","xxtx"], #侠行天下
		      ["http://www.23wxx.com/0_461/","wxt"], #五行天
		      ["http://www.23wxx.com/0_379/","haxsd"] #黑暗血时代
		     ]

		while 1:
			for data in dd:
				self.Timed_restart_time = time.localtime(time.time())
				self.save_mulu(data[0], os.path.join(CURRENTURL,'day')+os.path.sep,data[1])
			sys.stdout.write("程序完成等待60秒")
			sys.stdout.write("                                                   \r")
			sys.stdout.flush()
			time.sleep(60 * 5)
			sys.stdout.write("60秒完成")
			sys.stdout.write("                                                   \r")
			sys.stdout.flush()











	def save_mulu(self,url,filename,name):
		self.url = url
		self.filename = filename
		self.name = name
		str1 = "<dd><a href=\""
		str2 = ".html\">"
		str3 = "</a></dd>"
		content = http.urlopen(self.url).read()
		content = content.decode("gbk")
		content1 = content
		# content1 = content.split("王破来了")[1]


		str_lst = content1.split(str1)

		i_len = len(str_lst)
		i = 0
		ml_lst = set()



		if os.path.exists(self.filename+"ml"+os.path.sep+self.name+"ml.txt"):
			with open(self.filename+"ml"+os.path.sep+self.name+"ml.txt","r") as f:
				for data in f.readlines():
					ml_lst.add(data.strip())



		for strr in str_lst:
			i = i + 1
			strr_lst = strr.split(str2)
			if len(strr_lst) > 1:
				# print(strr_lst[0].split("/")[-1],strr_lst[1].split(str3)[0])
				if strr_lst[1].split(str3)[0] in ml_lst:
					continue
				if strr_lst[0].split("/")[-1] in ml_lst:
					continue
				sys.stdout.write("(%s\\%s)保存数据 %s                 "% (i,len(str_lst),strr_lst[1].split(str3)[0]))
				sys.stdout.write("\r")
				sys.stdout.flush()
				self.get_txt(strr_lst[0].split("/")[-1],strr_lst[1].split(str3)[0],i)
				with open(self.filename+"ml"+os.path.sep+self.name+"ml.txt","a") as f:
					f.write(strr_lst[1].split(str3)[0])
					f.write("\n")
					f.write(strr_lst[0].split("/")[-1])
					f.write("\n")
				


	def get_mulu(self):
		str1 = "<dd><a href=\""
		str2 = ".html\">"
		str3 = "</a></dd>"
		content = http.urlopen(self.url).read()
		content = content.decode("gbk")
		content1 = content.split("王破来了")[1]


		str_lst = content1.split(str1)

		i_len = len(str_lst)
		i = 0
		for strr in str_lst:
			i = i + 1
			strr_lst = strr.split(str2)
			if len(strr_lst) > 1:
				sys.stdout.write("保存数据 %s/%s                 "% (i , i_len))
				sys.stdout.write("\r")
				sys.stdout.flush()

				t1 = threading.Thread(target=self.get_txt, args=(strr_lst[0].split("/")[-1],strr_lst[1].split(str3)[0],i) )
				t1.start()

	def get_txt(self,num,strr,i):
		self.Timed_restart_time = time.localtime(time.time())
		time_now_str = time.strftime('%Y%m%d ',time.localtime(time.time()))
		str1 = "<div id=\"content\">"
		str2 = "<div class=\"bottem2\">"


		str3 = "&nbsp;&nbsp;&nbsp;&nbsp;，()，( "
		str4 = "http://www.23wxx.com/"
		str5 = "/ 移动版阅读m.23wxx.com )</div>"
		str6 = "<script>read3();</script><script>bdshare();</script>"
		list_str = [str3,str4,str5,str6,
		"0_461","择天记" , "0_76","黑暗血时代  0_379","未完待续" 	]





		str_url = self.url + num + ".html"
		content = http.urlopen(str_url).read()
		# print(content[100])
		content = content.decode("gbk")
		# content = str(content , "utf8")

		# findPart(u"#[\w\u2E80-\u9FFF]+#", content, "unicode chinese")
		content1 = str(content).split(str1)[1]
		content1 = content1.split(str2)[0]
		content1 = str_replace(content1,list_str)


		content1 = content1.replace("&nbsp;&nbsp;&nbsp;&nbsp;","")
		content1 = content1.replace("<br />","")
		content1 = strr + "\n" + content1
		with open(self.filename + time_now_str + ""+self.name +str(i).zfill(4)+ " " + strr + ".txt","w") as f:
			f.write(content1)


# while_run(run)

x = run_class()
Timed_restart(x,300*2,"16_get_xiaoshuo")
# http://www.23wxx.com/0_76/