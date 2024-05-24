from multiprocessing import Process


num = []

def func_process_1():
    global num
    num.extend([1,2,3])
    print(num)

def func_process_2():
    global num
    num.extend([4,5,6])
    print(num)
    
if __name__ == '__main__':    
    
    p1 = Process(target=func_process_1)
    p2 = Process(target=func_process_2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(num)