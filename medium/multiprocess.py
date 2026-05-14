import multiprocessing as pr
import queue
import time
cq = pr.Queue()
cq.put("mission A")
cq.put("mission B")
def Gen(q,st):
    data = q.get()
    print(data)
    time.sleep(st)
    
if __name__ == "__main__":
    pr1 = pr.Process(target=Gen,args=(cq,3))
    pr2 = pr.Process(target=Gen,args=(cq,1))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()
    print("end")
    