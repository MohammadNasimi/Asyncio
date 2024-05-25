from time import sleep,perf_counter
from threading import Thread

def show(name):
    print(f"starting {name}")
    sleep(3)
    print(f"starting {name}")
    

start = perf_counter()

t1 = Thread(target=show,args=('hassan',))
t2 = Thread(target=show,args=('mmad',))

t1.start()  
t2.start() 

t1.join() # wait until thead terminate 
t2.join()

end = perf_counter()
print(end -start)