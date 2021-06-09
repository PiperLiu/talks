# -*- coding: utf-8 -*-

from euler_task import euler_func, timer

import ray

from typing import List

ST_NUM: int = 300
EN_NUM: int = 800
MP_NUM: int = 8

ray.init()

def fill_task_queue() -> List[List[int]]:
    rts = []
    for i in range(ST_NUM, EN_NUM):
        rt = list(range(ST_NUM + i, EN_NUM, MP_NUM))
        rts.append(rt)
    return rts

@ray.remote
def calc(task: List[int]) -> List:
    rts = []
    for i in task:
        rt = euler_func(i)
    rts.append(rt)

def init_rays(task_queue: List[int]):
    def inner_func():
        ids = []
        for i in range(MP_NUM):
            task = task_queue[i]
            ray_id = calc.remote(task)
            ids.append(ray_id)
        return ids
    return inner_func

def get_results(ids: List, output_queue: List[int]):
    for i in ids:
        rt = ray.get(i)
        output_queue.append(rt)

if __name__ == '__main__':
    task_q = fill_task_queue()
    outp_q = []

    inner_func = init_rays(task_q)

    @timer
    def ray_func():
        ids = inner_func()
        get_results(ids, outp_q)

    ray_func()
