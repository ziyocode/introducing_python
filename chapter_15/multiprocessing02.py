import multiprocessing
import time
import os


def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))
    time.sleep(4)


def loopy(name):
    whoami(name)
    start = 1
    stop = 10000000
    for num in range(start, stop):
        pid = os.getpid()
        print("PID: %s \tNumber %s of %s. Honk!" % (pid, num, stop))


if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()


# multiprocessing.Process 한 프로그램 내에서 별도의 프로세스로 실행하거나 한 프로그램에서
# 독립적인 여러 프로새스를 실행