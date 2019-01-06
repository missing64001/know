# import asyncio,random
# @asyncio.coroutine
# def smart_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0, 0.2)
#         yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
#         print('Smart one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1
 


# @asyncio.coroutine
# def stupid_fib(n):
#     index = 0
#     a = 0
#     b = 1
#     while index < n:
#         sleep_secs = random.uniform(0, 0.4)
#         yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
#         print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
#         a, b = b, a + b
#         index += 1
 
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [
#         smart_fib(10),
#         stupid_fib(10),
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print('All fib finished.')
#     loop.close()




# import time,asyncio,random
# async def mygen(alist):
#     while len(alist) > 0:
#         c = random.randint(0, len(alist)-1)
#         print(alist.pop(c))
#         await asyncio.sleep(1)
# strlist = ["ss","dd","gg"]
# intlist=[1,2,5,6]
# c1=mygen(strlist)
# c2=mygen(intlist)
# print(c1)

# if __name__ == '__main__':
#         loop = asyncio.get_event_loop()
#         tasks = [
#         c1,
#         c2
#         ]
#         loop.run_until_complete(asyncio.wait(tasks))
#         print('All fib finished.')
#         loop.close()




# # main.py
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # Python基础-异步IO的支持 async和await

# # asyncio的编程模型就是一个消息循环
# import threading
# import asyncio
# from multiprocessing import Process

# # 把 generator 标记为 coroutine 类型，便于执行 EventLoop
# async def func(name):
#     print('Start %s! (%s)' % (name, threading.currentThread()))
#     # yield from语法可以让我们方便地调用另一个generator
#     if name == "访问百度":
#         print("%s 延迟 1秒" % name)
#         await asyncio.sleep(1)
#     elif name == "访问Google":
#         print("%s 延迟 5秒" % name)
#         await asyncio.sleep(5)
#     else:
#         print("%s 延迟 3秒" % name)
#         await asyncio.sleep(3)

#     print('\n End %s!! (%s)' % (name, threading.currentThread()))


# # 获取 EventLoop
# loop = asyncio.get_event_loop()

# tasks = [func("访问百度"),func("访问Google"),func("访问Python")]

# # 执行 coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# # print(dir(loop))
# loop.close()



# ---------------------------------------------------
# main.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python基础-异步IO的支持 async和await

# asyncio的编程模型就是一个消息循环
import threading
import asyncio
from multiprocessing import Process

# 把 generator 标记为 coroutine 类型，便于执行 EventLoop
async def func(name):
    print('Start %s! (%s)' % (name, threading.currentThread()))
    # yield from语法可以让我们方便地调用另一个generator
    if name == "访问百度":
        print("%s 延迟 1秒" % name)
        await asyncio.sleep(1)
    elif name == "访问Google":
        print("%s 延迟 5秒" % name)
        await asyncio.sleep(5)
    else:
        print("%s 延迟 3秒" % name)
        await asyncio.sleep(3)

    print('\n End %s!! (%s)' % (name, threading.currentThread()))

def mm(tasks):
    # 获取 EventLoop
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()


    # 执行 coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    # print(dir(loop))
    loop.close()
    

tasks = [func("访问百度"),func("访问Google"),func("访问Python")]
p = threading.Thread(target=mm, args=(tasks,))
# p = Process(target=mm, args=(tasks,))
p.start()
print('hahahahahaha ')
p.join()
# 
# 
# mm(tasks)
print('Child process end.')