import sys


def print_usage():
    print("Usage: python operations.py <number1> <number2> \
\nExample:\n\tpython operations.py 10 3")


def print_results(a, b):
    print(f"Sum:\t\t{a + b}")
    print(f"Difference:\t{a - b}")
    print(f"Product:\t{a * b}")
    if (b):
        print(f"Quotient:\t{a / b}")
    else:
        print("Quotient:\tERROR (div by zero)")
    if (b):
        print(f"Remainder:\t{a % b}")
    else:
        print("Remainder:\tERROR (modulo by zero)")


def main(argv):
    if len(argv) == 3:
        arg1 = argv[1]
        arg2 = argv[2]
        if (arg1.isnumeric() and arg2.isnumeric()):
            print_results(int(arg1), int(arg2))
        else:
            print("InputError: only numbers\n")
            print_usage()
    elif len(argv) > 3:
        print('InputError: too many arguments\n')
        print_usage()
    else:
        print_usage()


if __name__ == '__main__':
    main(sys.argv)
