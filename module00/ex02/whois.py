import sys


def main(argv):
    if len(argv) == 2:
        arg = argv[1]
        if (arg.isnumeric()):
            arg = int(arg)
            if (arg == 0):
                print("I'm Zero.")
            elif (arg % 2):
                print("I'm Odd.")
            else:
                print("I'm Even.")
        else:
            print("ERROR")
    elif len(argv) > 2:
        print('ERROR')


if __name__ == '__main__':
    main(sys.argv)
