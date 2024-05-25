from time import sleep,perf_counter
from threading import Thread,current_thread,enumerate

def show(name):
    print(current_thread())
    print(current_thread().getName,current_thread().ident)
    print(enumerate())
    print(f"starting {name}")
    sleep(3)
    print(f"starting {name}")
    

start = perf_counter()

t1 = Thread(target=show,args=('hassan',),name='first',)
t2 = Thread(target=show,args=('mmad',))


# print(t1.isDaemon(True))
# print(t2.isDaemon(True))

t1.start()  
t2.start() 

t1.join() # wait until thead terminate 
t2.join()

# print(t1.isDaemon())
# print(t2.isDaemon())

end = perf_counter()
print(end -start)