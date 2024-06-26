"""
    race condition
    thread safe
    dead lock
    
"""

from threading import Thread,Lock


num = 0 # share recource

lock = Lock()

def add():
    global num
    lock.acquire()
    for _ in range(100000):
        num +=1
    lock.release()
    
def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -=1
            

t1 = Thread(target=add)
t2 = Thread(target=subtract)


t1.start()
t2.start()

t1.join()
t2.join()

print(num)
print("Done .....")