import multiprocessing as mp
from multiprocessing import freeze_support
import os


def washer(dishes, output) -> None:
    for dish in dishes:
        pid01 = os.getpid()
        print("PID:%d Washing" % (pid01), dish, "dish")
        output.put(dish)


def dryer(input) -> None:
    while True:
        dish = input.get()
        pid02 = os.getpid()
        print("PID:%d Drying" % (pid02), dish, "dish")
        input.task_done()


if __name__=="__main__":
    freeze_support()
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ["salad", "bread", "entree", "dessert"]
    washer(dishes, dish_queue)
    dish_queue.join()


# multiprocessing은 JoinableQueue() 로 dryer_proc과 연결
# output.put(dish)로 JoinableQueue object에 기록 --> <multiprocessing.queues.JoinableQueue object at 0x10c86ed00>  
# input.get()으로 JoinableQueue object에서 가져오기

