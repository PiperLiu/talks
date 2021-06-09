from euler_task import euler_func, timer

ST_NUM: int = 300
EN_NUM: int = 800

@timer
def linear_euler():
    for i in range(ST_NUM, EN_NUM):
        euler_func(i)

if __name__ == '__main__':
    linear_euler()
