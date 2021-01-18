import sys


def main(argv):
    if len(argv) == 3:
        text = argv[1]
        length = argv[2]
        if ((not text.isnumeric()) and length.isnumeric()):
            length = int(length)
            for punct in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                text = text.replace(punct, ' ')
            flist = [word for word in text.split() if len(word) > length]
            print(flist)
        else:
            print("ERROR")
    else:
        print('ERROR')


if __name__ == '__main__':
    main(sys.argv)
