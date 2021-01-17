def is_punctuation_mark(char):
    return (char in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")


def analyze(text, length):
    print(f"The text contains {length} characters:")
    print(f"- {sum([char.isupper() for char in text])} upper letters")
    print(f"- {sum([char.islower() for char in text])} lower letters")
    print(f"- {sum([is_punctuation_mark(char) for char in text])} \
punctuation marks")
    print(f"- {text.count(' ')} spaces")


def text_analyzer(*args):
    """
This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text.
    """
    if (len(args) > 1):
        print("ERROR")
    elif (len(args) == 0):
        text = input("What is the text to analyse?\n>> ")
        analyze(text, len(text))
    else:
        length = len(args[0])
        if (length == 0):
            print("The text is empty")
        else:
            analyze(args[0], length)
