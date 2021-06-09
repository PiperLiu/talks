from euler_task import euler_func, timer

import threading
import queue

from typing import List

ST_NUM: int = 300
EN_NUM: int = 800
TD_NUM: int = 8

def fill_task_queue():
    q = queue.Queue()
    for i in range(ST_NUM, EN_NUM):
        q.put(i)
    return q

def thread_task(task_queue: queue.Queue, output_queue: queue.Queue, queue_lock: threading.Lock):
    while not task_queue.empty():

        queue_lock.acquire()
        data = task_queue.get()
        queue_lock.release()

        retu = euler_func(data)

        queue_lock.acquire()
        output_queue.put(retu)
        queue_lock.release()

        # print(f'task_queue size: {task_queue.qsize()}')
        # print(f'output_queue size: {output_queue.qsize()}')

def init_threads(task_queue: queue.Queue, output_queue: queue.Queue, queue_lock: threading.Lock) -> List[threading.Thread]:
    threads = []
    for _ in range(TD_NUM):
        th = threading.Thread(target=thread_task, args=[task_queue, output_queue, queue_lock])
        threads.append(th)
    return threads

def get_thread_func(threads: List[threading.Thread]):
    def inner_func():
        for th in threads:
            th.start()
        for th in threads:
            th.join()
    return inner_func

if __name__ == '__main__':
    task_q = fill_task_queue()
    outp_q = queue.Queue()
    queue_lock = threading.Lock()
    threads = init_threads(task_q, outp_q, queue_lock)

    inner_multithreading = get_thread_func(threads)

    @timer
    def multithreading():
        inner_multithreading()
    
    multithreading()
