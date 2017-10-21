from multiprocessing import Process, Queue



def f1(queue):
    queue.put([1,2,3])

def f2(queue1,queue2):
    data = queue1.get()
    print(data)
    data = [x*x for x in data]
    queue2.put(data)

def f3(queue):
    data = queue.get()
    print(data)

def main(queue1,queue2):
    p1 = Process(target=f1,args=(queue1,))
    p2 = Process(target=f2,args=(queue1,queue2))
    p3 = Process(target=f3,args=(queue2,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

if __name__ == '__main__':
    queue1 = Queue()
    queue2 = Queue()
    main(queue1,queue2)