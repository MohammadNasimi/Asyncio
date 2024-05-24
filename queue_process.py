from multiprocessing import Process ,Queue


numbers = []

def func_process_1(queue):
    num = queue.get()
    num.extend([1,2,3])
    queue.put(num)
    print(num)

def func_process_2(queue):
    num = queue.get()
    num.extend([4,5,6])
    queue.put(num)
    print(num)
    
if __name__ == '__main__':    
    qs = Queue()
    qs.put(numbers)
    p1 = Process(target=func_process_1,args=(qs, ))
    p2 = Process(target=func_process_2,args=(qs, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(qs.get())
    
    
    """result:
                [1, 2, 3]
                [4, 5, 6]
                []
            process have split memory ---> we can connect memeory process with values and array 
        after use Queue 
        [1, 2, 3, 4, 5, 6]
    """ 