class Matrix:
    def __init__(self, *args):
        if (len(args) == 2):
            if (type(args[0]) is not list):
                exit()
            for row in args[0]:
                if (type(row) is not list):
                    exit()
                if (len(row) != len(args[0][0])):
                    exit()
                for elem in row:
                    if (type(elem) is not float):
                        exit()
            self.data = args[0]
            if (type(args[1]) is not tuple or len(args[1]) != 2):
                exit()
            if (type(args[1][0]) is not int or type(args[1][1]) is not int
                    or args[1][0] < 0 or args[1][1] < 0):
                exit()
            self.shape = args[1]
        elif (len(args) == 1):
            arg = args[0]
            if (type(arg) is list):
                for row in arg:
                    if (type(row) is not list):
                        exit()
                    for elem in row:
                        if (type(elem) is not float):
                            exit()
                self.data = arg
                self.shape = (len(arg), len(arg[0]))
                for row in arg:
                    if (len(row) != self.shape[1]):
                        exit()
            elif (type(arg) is tuple):
                if (len(arg) == 2):
                    if (type(arg[0]) is not int or type(arg[1]) is not int
                            or arg[0] < 0 or arg[1] < 0):
                        exit()
                    self.shape = arg
                    self.data = [[0.0] * arg[1] for i in range(arg[0])]
                else:
                    exit()
            else:
                exit()
        else:
            exit()

        # print(self.__dict__)

    def __str__(self):
        txt = str(self.data)
        return f"(Matrix {txt})"

    def __repr__(self):
        txt = str(self.data)
        return f"(Matrix{self.shape} {txt})"

    def __add__(self, operand):
        if (type(operand) is Matrix):
            pass
        elif (type(operand) is int or type(operand) is float):
            data = [[self.data[j][i] + operand for i in range(self.shape[0])] for j in range(self.shape[1])]
            return Matrix(data)
