#!/usr/bin/env python3

import os



# 从 multiprocessing 中导入 Process 类
from multiprocessing import Process

def hello(name):
    print('child precess:{}'.format(os.getpid()))
    print('hello'+name,sep='')

def main():
    p = Process(target=hello,args=('shiyanlou', ))
    p.start()
    p.join()
    print('parent process:{}'.format(os.getppid()))

'''
在 main 函数中，用 Process 类定义了一个子进程，这个子进程要执行的函数是 hello，传入的参数是 shiyanlou，然后调用 start() 方法，启动子进程，这时候子进程会调用 hello 函数，将 shiyanlou 作为参数传入，打印当前进程 id 和 hello shiyanlou 后返回。 
join() 方法表示等待子进程运行结束后继续执行，所以在子进程返回后会继续打印父进程的 id。
'''

if __name__ == '__main__':
    main()

#进程间通信pipe

from multiprocessing import Process, Pipe

conn1, conn2 = Pipe()

def f1():
    conn1.send('Hello shiyanlou')

def f2():
    data = conn2.recv()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()
'''
这个程序启动了俩个进程，第一个进程在 f1 函数中向 pipe 管道写入 Hello shiyanlou，第二个进程在 f2 函数中从管道中读取数据并打印。
'''

#进程间通信queue
from multiprocessing import Process, Queue

queue = Queue()

def f1():
    queue.put('Hello shiyanlou')

def f2():
    data = queue.get()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main()

#进程同步
import time
from multiprocessing import Process,Value,Lock

def func(val):
    for i in range(50):
        time.sleep(0.01)
        lock.acquire()
        val.value += 1
        lock.release()

if __name__ == '__main__':
    # 多进程无法使用全局变量，multiprocessing 提供的 Value 是一个代理器，
    # 可以实现在多进程的共享这个变量
    v = Value('i',0)
    # 初始化锁
    lock = Lock()
    #创建10个进程
    procs = [Process(target=func,args=(v,)) for i in range(10)]

    for p in procs:
        p.start()
    
    for p in procs:
        p.join()
    
    print(v.value)

# 进程池

from multiprocessing import Pool

def f(i):
    print(i,end='\n')

def main():
    #初始化一个3个进程的进程池
    pool = Pool(processes=3)
    for i in range(30):
        pool.apply(f,(i,))

if __name__ == '__main__':
    main()

# 多线程（推荐使用多进程）
'''
由于 GIL 的存在，Python 的多线程实际上还是在一个 CPU 的核心上跑，也就是它不能充分利用 CPU 的多核。所以在实际使用中还是推荐使用多进程。
'''
import threading

def hello(name):
      # get_ident() 函数获取当前线程 id 
    print('child thread: {}'.format(threading.get_ident()))
    print('Hello ' + name)

def main():
    # 初始化一个线程，参数传递和使用 Process 一样
    t = threading.Thread(target=hello, args=('shiyanlou',))
    # 启动线程和等待线程结束，和 Process 的接口一样
    t.start()
    t.join()
    print('main thread: {}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()