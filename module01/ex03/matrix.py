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
            if (len(arg) != 2 or type(arg[0]) is not int
                    or type(arg[1]) is not int):
                exit()
            self.size = arg[1] - arg[0]
            if (self.size < 0):
                exit()
            self.values = [0.0 + i for i in range(arg[0], arg[1])]
        else:
            exit()

    def __repr__(self):
        txt = str(self.values)
        return f"(Vector({self.size}) {txt})"

    def __str__(self):
        txt = str(self.values)
        return f"(Vector {txt})"

    def __add__(self, operand):
        if (type(operand) is Vector):
            if (operand.size != self.size):
                exit()
            values = [self.values[i] + operand.values[i]
                      for i in range(self.size)]
            return Vector(values)
        elif (type(operand) is int or type(operand) is float):
            values = [self.values[i] + operand for i in range(self.size)]
            return Vector(values)

    __radd__ = __add__

    def __sub__(self, operand):
        if (type(operand) is Vector):
            if (operand.size != self.size):
                exit()
            values = [self.values[i] - operand.values[i]
                      for i in range(self.size)]
            return Vector(values)
        elif (type(operand) is int or type(operand) is float):
            values = [self.values[i] - operand for i in range(self.size)]
            return Vector(values)

    def __rsub__(self, operand):
        if (type(operand) is Vector):
            if (operand.size != self.size):
                exit()
            values = [operand.values[i] - self.values[i]
                      for i in range(self.size)]
            return Vector(values)
        elif (type(operand) is int or type(operand) is float):
            values = [operand - self.values[i] for i in range(self.size)]
            return Vector(values)

    def __mul__(self, operand):
        if (type(operand) is Vector):
            if (operand.size != self.size):
                exit()
            dot_product = sum([self.values[i] * operand.values[i]
                              for i in range(self.size)])
            return dot_product
        elif (type(operand) is int or type(operand) is float):
            values = [self.values[i] * operand for i in range(self.size)]
            return Vector(values)

    __rmul__ = __mul__

    def __truediv__(self, operand):
        if ((type(operand) is int or type(operand) is float) and operand):
            values = [self.values[i] / operand for i in range(self.size)]
            return Vector(values)
        else:
            exit()

    def __rtruediv__(self, operand):
        if (type(operand) is int or type(operand) is float):
            for elem in self.values:
                if not elem:
                    exit()
            values = [operand / self.values[i] for i in range(self.size)]
            return Vector(values)
        else:
            exit()


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

    def __str__(self):
        txt = str(self.data)
        return f"(Matrix {txt})"

    def __repr__(self):
        txt = str(self.data)
        return f"(Matrix{self.shape} {txt})"

    def __add__(self, operand):
        if (type(operand) is Matrix and operand.shape == self.shape):
            data = [[self.data[j][i] + operand.data[j][i]
                    for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)
        elif (type(operand) is int or type(operand) is float):
            data = [[self.data[j][i] + operand for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    __radd__ = __add__

    def __sub__(self, operand):
        if (type(operand) is Matrix and operand.shape == self.shape):
            data = [[self.data[j][i] - operand.data[j][i]
                    for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)
        elif (type(operand) is int or type(operand) is float):
            data = [[self.data[j][i] - operand for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    def __rsub__(self, operand):
        if (type(operand) is Matrix and operand.shape == self.shape):
            data = [[operand.data[j][i] - self.data[j][i]
                    for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)
        elif (type(operand) is int or type(operand) is float):
            data = [[operand - self.data[j][i] for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    def __truediv__(self, operand):
        if (type(operand) is int or type(operand) is float and operand):
            data = [[self.data[j][i] / operand for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    def __rtruediv__(self, operand):
        if (type(operand) is int or type(operand) is float):
            for row in self.data:
                if 0.0 in row:
                    exit()
            data = [[operand / self.data[j][i] for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    def __mul__(self, operand):
        if (type(operand) is Matrix and operand.shape[0] == self.shape[1]):
            data = [[sum([self.data[j][k] * operand.data[k][i]
                    for k in range(self.shape[1])])
                    for i in range(operand.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)
        elif (type(operand) is Vector and operand.size == self.shape[1]):
            values = [sum([self.data[i][j] * operand.values[j]
                           for j in range(self.shape[1])])
                      for i in range(self.shape[0])]
            return Vector(values)
        elif (type(operand) is int or type(operand) is float):
            data = [[self.data[j][i] * operand for i in range(self.shape[1])]
                    for j in range(self.shape[0])]
            return Matrix(data)

    __rmul__ = __mul__
