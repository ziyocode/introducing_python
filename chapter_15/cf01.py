from concurrent import futures
import math
import time
import sys


def calc(val):
    time.sleep(1)
    result = math.sqrt(float(val))
    return result


def use_threads(num, values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        results = tex.map(calc, values)
    t2 = time.time()
    return t1 - t2


def use_processes(num, values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as pex:
        results = pex.map(calc, values)
    t2 = time.time()
    return t1 - t2


def main(workers, values):
    print(f"Using {workers} workers for {len(values)} values")
    t_sec = use_threads(workers, values)
    print(f"Threads took {t_sec:.4f} seconds")
    p_sec = use_processes(workers, values)
    print(f"Processes took {p_sec:.4f} seconds")


if __name__ == "__main__":
    workers = int(sys.argv[1])      # 명령행에서 첫번째 arguemnt
    values = list(range(1, 6))      # 1, 2, 3, 4, 5
    print(f"workers : {workers} / values : {values}")
    main(workers, values)

# Using 1 workers for 5 values
# Threads took -5.0122 seconds
# Processes took -5.1588 seconds
