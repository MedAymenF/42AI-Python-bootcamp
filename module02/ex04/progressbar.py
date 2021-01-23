from time import sleep
import os


def progressbar(lst):
    length = len(lst)
    for i in lst:
        os.system('clear')
        progress = (i + 1) * 100 // length
        print("[{:3}%]".format(progress), end=' ')
        print("[{:25}]".format("=" * (24 * progress // 100) + ">"), end=' ')
        print(f"{i}/{length}")
        yield i
