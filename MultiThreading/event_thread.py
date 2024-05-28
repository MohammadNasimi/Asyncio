from threading import Thread, Event
from time import sleep


def first(f,s):
    sleep(5)
    print("ready thread first")
    f.set()
    s.wait()
    print("working thread first")
    f.clear()
    
def second(f,s):
    print("ready thread second")
    s.set()
    f.wait()
    print("working thread second")
    s.clear()
    
    
f = Event()
s = Event()


t1 = Thread(target=first,args=(f,s))
t2 = Thread(target=second,args=(f,s))

t1.start()
t2.start()