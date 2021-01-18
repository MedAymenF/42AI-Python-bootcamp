import sys

ALNM = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }


def print_morse(arg, j):
    for i, char in enumerate(arg):
        if (i or j):
            print(' ', end='')
        print(ALNM[char], end='')


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        args = []
        for arg in sys.argv[1:]:
            args += arg.upper().split()
        for arg in args:
            if (not arg.isalnum()):
                print(f"ERROR")
                exit()
        for i, arg in enumerate(args):
            if (i):
                print(' /', end='')
            print_morse(arg, i)
        print('')
