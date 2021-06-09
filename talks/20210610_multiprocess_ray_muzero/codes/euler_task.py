from functools import wraps
import time

def euler_func(n: int) -> int:
    res = n
    i = 2
    while i <= n // i:
        if n % i == 0:
            res = res // i * (i - 1)
            while (n % i == 0): n = n // i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res

def timer(func):
    @wraps(func)
    def inner_func():
        t = time.time()
        rts = func()
        print(f"timer: using {time.time() - t :.5f} s")
        return rts
    return inner_func

if __name__ == '__main__':
    # import time
    # from tqdm import trange
    # t = time.time()
    # for i in trange(5, 3000):
    #     euler_func(i)
    # print(time.time() - t)

    @timer
    def euler5000():
        for i in range(5, 5000):
            euler_func(i)
    
    euler5000()
