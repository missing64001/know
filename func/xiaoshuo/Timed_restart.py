#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,os

import sys,time

import urllib.request as http
import time, threading
import inspect
import ctypes
global my_time
from datetime import datetime, timedelta, timezone


def fprint(strr):
	sys.stdout.write(strr)
	sys.stdout.write("                         \r")
	sys.stdout.flush()

def _async_raise(tid, exctype):
	"""raises the exception, performs cleanup if needed"""
	tid = ctypes.c_long(tid)
	if not inspect.isclass(exctype):
		exctype = type(exctype)
	res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
	if res == 0:
		exit()
		raise #ValueError("invalid thread id")
	elif res != 1:
		# """if it returns a number greater than one, you're in trouble,
		# and you should call it again with exc=NULL to revert the effect"""
		ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
		exit()
		raise #SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
	if thread.is_alive():
		_async_raise(thread.ident, SystemExit)
	# if thread.is_alive():
	#     time.sleep(3)
	#     stop_thread(thread)

		
def stop_thread_lst(lst,idd = None):
	for t in lst:
		if t == idd:
			continue
		if lst[t].is_alive():
			stop_thread(lst[t])
def thread_lst_is_alive(lst):
	for t in lst:
		if lst[t].is_alive():
			return True
	return False

def run1(x):
	i = 0
	while 1:
		i += 1
		print(i,x)
		time.sleep(1)


def Timed_restart(run_class,timee=10,cmdname = "程序已运行",argss=()):


	t = threading.Thread(target=run_class.run, args=argss )
	t.start()
	time.sleep(2)
	zzz = 1 
	while zzz:

		# xxx = mysize(run_class,"run_class")
		# print("run_class",xxx)


		time_last_str = time.strftime('%Y-%m-%d %H:%M:%S',run_class.Timed_restart_time)
		time_now_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
		time_last = datetime.strptime(time_last_str, '%Y-%m-%d %H:%M:%S')
		time_now = datetime.strptime(time_now_str, '%Y-%m-%d %H:%M:%S')

		# sys.stdout.write("程序已运行：%s，%s秒内未完成则重启"%(time_now - time_last,timee))
		# sys.stdout.write("                         \r")
		# sys.stdout.flush()
		strrr = ("：%s，%s秒内未完成则重启"%(time_now - time_last,timee))


		# os.system("title " + cmdname + " " + strrr)
		if not "threading_lst" in dir(run_class):
			run_class.threading_lst = []
		if not "id" in dir(run_class):
			run_class.id = -1

		threading_lst = run_class.threading_lst


		threading_is_alive = -1
		if run_class.id != -1:
			stop_thread_lst(threading_lst,run_class.id)
			threading_is_alive = threading_lst[run_class.id].is_alive()

		if time_last + timedelta(seconds=timee) < time_now:
			print("到时间   ")
			if t.is_alive():
				print("程序未完成")
				stop_thread(t)
			stop_thread_lst(threading_lst)



			linshi_lst = []
			if not "old_threading_lst" in dir(run_class):
				run_class.old_threading_lst = []
			for da in threading_lst:
				if threading_lst[da].is_alive():
					# print("XXXXXXXXXXX",threading_lst[da])
					run_class.old_threading_lst.append(threading_lst[da])

			for da in run_class.old_threading_lst:
				linshi_lst.append(da)
			for da in linshi_lst:
				stop_thread(da)


				if da.is_alive():
					# print(da.getName(),da)
					# if "pmy" in dir(run_class):
						# run_class.pmy.astr(str([da.getName()]),True)


					run_class.old_threading_lst.remove(da)
			int_i = len(run_class.old_threading_lst)
			if int_i:
				fprint("old_threading_lst:"+str(int_i))
			else:
				fprint("old_threading_lst:"+str(int_i))



			t = threading.Thread(target=run_class.run, args=argss )
			run_class.Timed_restart_time = time.localtime(time.time())
			t.start()
		# elif not(t.is_alive()) and not(thread_lst_is_alive(threading_lst)):
		
		elif not(t.is_alive()) and not(threading_is_alive):


			linshi_lst = []
			if not "old_threading_lst" in dir(run_class):
				run_class.old_threading_lst = []
			for da in threading_lst:
				if threading_lst[da].is_alive():
					# print("XXXXXXXXXXX",threading_lst[da])
					run_class.old_threading_lst.append(threading_lst[da])

			for da in run_class.old_threading_lst:
				linshi_lst.append(da)
			for da in linshi_lst:
				stop_thread(da)
				if da.is_alive():
					# print(da.getName(),da)
					# if "pmy" in dir(run_class):
						# run_class.pmy.astr(str([da.getName()]),True)
					run_class.old_threading_lst.remove(da)
			int_i = len(run_class.old_threading_lst)
			if int_i:
				fprint("old_threading_lst:"+str(int_i))
			else:
				fprint("old_threading_lst:"+str(int_i))





			t = threading.Thread(target=run_class.run, args=argss )
			run_class.Timed_restart_time = time.localtime(time.time())
			t.start()

		time.sleep(1)



	# for i in range(timee):
	# 	if not(t.is_alive()):
	# 		Timed_restart(run_class,argss=argss)
	# 	time.sleep(1)
	# Timed_restart(run_class,argss=argss)
class run_class(object):
	def __init__(self):
		self.Timed_restart_time = time.localtime(time.time())
	def run(self):
		self.Timed_restart_time = time.localtime(time.time())
		i = 0
		while 1:
			i += 1
			print(i)
			time.sleep(1)


# xx = run_class()
# Timed_restart(xx,5,cmdname = "test")


# Timed_restart(run3,10,argss=("xx","CCV","efebgg"))
# 
# 
# 
# 
# 

# for example
# import sys
# sys.path.append("F:\\python\\00_little_tools")
# import Timed_restart
# from Timed_restart import Timed_restart


# class run_class(object):
#     def __init__(self,Config = None):
#         self.Timed_restart_time = time.localtime(time.time())
#         self.Config = Config
#     def run(self):
# 		self.Timed_restart_time = time.localtime(time.time())
#         for i in range(1,5):
#             t = threading.Thread(target=self.run_1, args=(i,) )
#             t.start()
#             time.sleep(1)


#     def run_1(self,ii):
#         i = 0
#         while 1:
#             i += 1
#             print(ii,i)
#             time.sleep(1)


# x = run_class()
# # x.run()
# Timed_restart(x,10)