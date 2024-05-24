from multiprocessing import Process ,Pool,cpu_count
from concurrent.futures import ProcessPoolExecutor

import time 

def init():
    print(" run show")

def show (name:str):
    print(f"starting  game {name}")
    time.sleep(3)
    print(f"Ending  game {name}")


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        names =['ali','hassan','mmad','borojali']
        executor.map(show,names)
        
    # pool
    names =['ali','hassan','mmad','borojali']
    pool = Pool(processes=cpu_count(),initializer=init)
    pool.map(show,names)


if __name__ == '__main__':    
    main()
    print(cpu_count())









