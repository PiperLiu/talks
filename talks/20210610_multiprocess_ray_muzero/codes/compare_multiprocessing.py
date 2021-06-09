from euler_task import euler_func, timer

import multiprocessing as mp

from typing import List

ST_NUM: int = 300
EN_NUM: int = 800
MP_NUM: int = 8

def fill_task_queue() -> mp.Queue():
    q = mp.Queue()
    for i in range(ST_NUM, EN_NUM):
        q.put(i)
    return q

def process_task(task_queue: mp.Queue, output_queue: mp.Queue):
    while not task_queue.empty():

        data = task_queue.get()
        retu = euler_func(data)
        output_queue.put(retu)

        # print(f'task_queue size: {task_queue.qsize()}')
        # print(f'output_queue size: {output_queue.qsize()}')

def init_proessors(task_queue: mp.Queue, output_queue: mp.Queue) -> List[mp.Process]:
    processors = []
    for _ in range(MP_NUM):
        processor = mp.Process(
            target=process_task,
            args=[task_queue, output_queue],
            daemon=True
        )
        processors.append(processor)
    return processors

def get_process_func(processors: List[mp.Process], task_queue: mp.Queue, output_queue: mp.Queue):
    size = task_queue.qsize()
    def inner_func():
        for processor in processors:
            processor.start()
        while True:
            if size == output_queue.qsize():
                for processor in processors:
                    processor.terminate()
                break
    return inner_func

if __name__ == '__main__':
    task_q = fill_task_queue()
    outp_q = mp.Queue()
    threads = init_proessors(task_q, outp_q)

    inner_multiprocessors = get_process_func(threads, task_q, outp_q)

    @timer
    def multiprocessors():
        inner_multiprocessors()

    multiprocessors()
