import sys


def main(argv):
    args = list(argv)
    del args[0]
    if (len(args)):
        string = " ".join(args)
        string = string.swapcase()
        string = string[::-1]
        print(string)


if __name__ == '__main__':
    main(sys.argv)
