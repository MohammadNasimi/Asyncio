from multiprocessing import Process , Lock


numbers = []

def func_process_add(num,lock):
    with lock:
        for _ in range(10000):
            num += 1

def func_process_minus(num,lock):
    lock.acquire()
    for _ in range(10000):
        num -= 1
    lock.release()
if __name__ == '__main__':    
    
    num=0 # shared resource between two process
    lock = Lock()
    p1 = Process(target=func_process_add,args=(num, lock))
    p2 = Process(target=func_process_minus,args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(num)
