class Vector:
    def __init__(self, arg):
        if (type(arg) is int):
            self.size = arg
            self.values = [0.0 + i for i in range(arg)]
        elif (type(arg) is list):
            for elem in arg:
                if (type(elem) is not float):
                    exit()
            self.size = len(arg)
            self.values = arg
        elif (type(arg) is tuple):
            if (len(arg) != 2 or type(arg[0]) is not int or type(arg[1]) is not int):
                exit()
            self.size = arg[1] - arg[0]
            if (self.size < 0):
                exit()
            self.values = [0.0 + i for i in range(arg[0], arg[1])]
        else:
            exit()

    def __repr__(self):
        txt = str(self.values)
        return txt

    def __str__(self):
        txt = str(self.values)
        return f"Vector ({txt})"
