from time import sleep
import os


def ft_progress(lst):
    length = len(lst)
    for i in lst:
        os.system('clear')
        progress = (i + 1) * 100 // length
        print("[{:3}%]".format(progress), end=' ')
        print("[{:25}]".format("=" * (24 * progress // 100) + ">"), end=' ')
        print(f"{i}/{length}")
        yield i


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
