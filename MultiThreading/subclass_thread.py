from time import sleep,perf_counter
from threading import Thread

def show(name,delay):
    print(f"starting {name}")
    sleep(delay)
    print(f"finish {name}")

class showThread(Thread):
    def __init__(self,name,delay):
        super().__init__()
        self.name = name
        self.delay = delay
    
    def run(self):
        show(self.name,self.delay)

start = perf_counter()

t1 = showThread("hassn",3)
t2 = showThread("mmad",5)

t1.start()  
t2.start() 

t1.join() # wait until thead terminate 
t2.join()

end = perf_counter()
print(end -start)