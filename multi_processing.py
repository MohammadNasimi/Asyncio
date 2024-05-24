from multiprocessing import Process

import time 




def show (name:str):
    print(f"starting  game {name}")
    time.sleep(3)
    print(f"Ending  game {name}")


# show("hassan")
# show("mmad")
# show("ali")
if __name__ == '__main__':    
    start = time.perf_counter()

    p = Process(target=show, args=('hassan',))
    p1 = Process(target=show, args=('mmad',))
    p2 = Process(target=show, args=('ali',))


    p.start()
    p1.start()
    p2.start()

    p.join() # finish process after run continue programe
    p1.join()
    p2.join()


    end = time.perf_counter()


    run_time = end - start

    print(run_time)
