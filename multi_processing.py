from multiprocessing import Process,current_process

import time 

import os


def show (name:str):
    print(f"starting  game {name}")
    time.sleep(3)
    print(f"Ending  game {name}")
    print(f"{name} pid",os.getpid()) # process id
    print(f"{name} ppid",os.getppid()) # parent process id
    print(f"{name}",current_process())


# show("hassan")
# show("mmad")
# show("ali")
if __name__ == '__main__':    
    start = time.perf_counter()

    p = Process(target=show, args=('hassan',),name = "hassan process")
    p1 = Process(target=show, args=('mmad',))
    p2 = Process(target=show, args=('ali',))


    p.start()
    p1.start()
    p2.start()
    
    print(p.is_alive()) # check now process run or not

    p.join() # finish process after run continue programe
    p1.join()
    p2.join()

    print(p1.is_alive()) # check now process run or not

    end = time.perf_counter()


    run_time = end - start

    print(run_time)
