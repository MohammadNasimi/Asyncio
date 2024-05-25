from concurrent.futures import ThreadPoolExecutor
from time import sleep


 
def show(x):
    print(f"number:{x}")
    sleep(3)
    print(f"finish:{x}")
    
 
if __name__ == '__main__':
    result =[]
    with ThreadPoolExecutor(max_workers=5) as executer:
        values = [3,4,5,6]
        result = executer.map(show,values)
     
    for r in result:
        print(r)