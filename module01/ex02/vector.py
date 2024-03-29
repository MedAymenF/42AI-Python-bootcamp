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
