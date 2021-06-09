from typing import List
from euler_task import euler_func, timer

import threading as th
import multiprocessing as mp

task1 = list(range(2, 50000, 3))  # 2, 5, ...
task2 = list(range(3, 50000, 3))  # 3, 6, ...
task3 = list(range(4, 50000, 3))  # 4, 7, ...

def job(task: List):
    for t in task:
        euler_func(t)

@timer
def normal():
    job(task1)
    job(task2)
    job(task3)

@timer
def mutlthread():
    th1 = th.Thread(target=job, args=(task1, ))
    th2 = th.Thread(target=job, args=(task2, ))
    th3 = th.Thread(target=job, args=(task3, ))

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

@timer
def multcore():
    p1 = mp.Process(target=job, args=(task1, ))
    p2 = mp.Process(target=job, args=(task2, ))
    p3 = mp.Process(target=job, args=(task3, ))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == '__main__':

    print("同步串行：")
    normal()

    print("多线程并发：")
    mutlthread()

    print("多进程并行：")
    multcore()
