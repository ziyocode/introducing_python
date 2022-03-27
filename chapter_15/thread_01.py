import threading


def do_this(what):
    whoami(what)


def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()


# Thread <_MainThread(MainThread, started 4446524928)> says: I'm the main program
# Thread <Thread(Thread-1, started 123145371758592)> says: I'm function 0
# Thread <Thread(Thread-2, started 123145371758592)> says: I'm function 1
# Thread <Thread(Thread-3, started 123145371758592)> says: I'm function 2
# Thread <Thread(Thread-4, started 123145371758592)> says: I'm function 3