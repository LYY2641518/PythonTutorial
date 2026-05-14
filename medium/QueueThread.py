#練習 以Queue來避免變數共用導致的race condition
import threading
import queue
import random
import time
order = queue.Queue()

order_list = ["雞","鴨","牛","豬","魚"]

def waiter():
    for i in range(40):
        dish = random.randint(0,4)
        order.put(dish)
        print(f"new order {order_list[dish]}")
        time.sleep(0.1)
    order.put(None)
    order.put(None)
        
def cooker(cook_speed,cook_name):
    while True:
        work = order.get()
        if work == None:
            order.task_done()
            break
        
        print(f"{cook_name}開始料理{order_list[work]}")
        time.sleep(cook_speed)
        order.task_done()
        print(f"{cook_name}料理{order_list[work]}完成")
    
thread1 = threading.Thread(target = waiter)
thread2 = threading.Thread(target = cooker,args=(0.5,"Jessie"))
thread3 = threading.Thread(target=cooker,args=(0.2,"Ben"))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
order.join()
thread2.join()
thread3.join()

print("下班囉")