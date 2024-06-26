from multiprocessing import Process,current_process

import time 

import os
import sys

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

    p = Process(target=show, args=('hassan',),name = "hassan process",daemon =True)
    p1 = Process(target=show, args=('mmad',),daemon =True)
    p2 = Process(target=show, args=('ali',),daemon =True)
    # daemon ignore finish process , important you need remove join for use daemon

    p.start()
    p1.start()
    p2.start()
    
    print(p.is_alive()) # check now process run or not

    # p.kill() # send sinal for stop process p 
    p.terminate() # send sinal for stop process p 
    
    p.join() # finish process after run continue programe
    p1.join()
    p2.join()

    print(p1.is_alive()) # check now process run or not

    print(p.exitcode)
    print(p.exitcode)
    """
    p.exitcode return number:
     0 ---> process complete
     more than 0  ----> process error
     less than 0 ----> process get signal with terminate or another thing 

                 -9 --> signal kill
                 -15 --> signal terminate
    """
    end = time.perf_counter()


    run_time = end - start

    print(run_time)

    sys.exit()