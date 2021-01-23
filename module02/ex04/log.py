import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        now = time.perf_counter()
        ret = func(*args, **kwargs)
        delta = time.perf_counter() - now
        f = open("machine.log", 'a')
        f.write(f"Running: {func.__name__}\t[ exec-time = {delta} s ]\n")
        f.close()
        return ret
    return wrapper
