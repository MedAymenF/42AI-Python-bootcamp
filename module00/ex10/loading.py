from time import sleep
import os


def ft_progress(lst):
    length = len(lst)
    for i in lst:
        os.system('clear')
        print("[{:3}%]".format((i + 1) * 100 // length), end=' ')
        print(f"{i}/{length}")
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    # print(f"elem = {elem}, ret = {ret}")
    sleep(0.01)
print()
print(ret)
