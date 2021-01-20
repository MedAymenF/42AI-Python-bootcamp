from random import randint


def generator(text, sep=" ", option=None):
    if (type(text) is not str):
        yield('ERROR')
    elif (option and option not in ["shuffle", "unique", "ordered"]):
        yield('ERROR')
    else:
        lst = text.split(sep=sep)
        if (option == "shuffle"):
            new_lst = []
            while len(lst):
                rand = randint(0, len(lst) - 1)
                new_lst.append(lst.pop(rand))
            lst = new_lst
        elif (option == "ordered"):
            lst.sort()
        elif (option == "unique"):
            lst = set(lst)
        for word in lst:
            yield word


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)

print('-' * 80)

for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print('-' * 80)

for word in generator(text, sep=" ", option="ordered"):
    print(word)

print('-' * 80)

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)

print('-' * 80)

text = 1.0
for word in generator(text, sep="."):
    print(word)
