from multiprocessing import Process

import time 

import os
from typing import Callable


def show (name:str,delay:int):
    print(f"starting  game {name}")
    time.sleep(delay)
    print(f"Ending  game {name}")


class showprocess(Process):
    def __init__(self,name_p,delay):
        super().__init__()
        self.name_p = name_p
        self.delay = delay
        
    def run(self):
        show(self.name_p,self.delay)
        
        
        
    
if __name__ == '__main__':    
    start = time.perf_counter()

    p = showprocess("hassan",4)
    p1 = showprocess("mmad",3)
    p2 = showprocess("ali",4)


    p.start()
    p1.start()
    p2.start()
    

    p.join() # finish process after run continue programe
    p1.join()
    p2.join()


    end = time.perf_counter()


    run_time = end - start

    print(run_time)
