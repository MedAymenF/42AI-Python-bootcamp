from matrix import Matrix, Vector


m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix((3, 3))
m3 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))
print(m3 + 10)
print(10 + m3)
print('-' * 80)
print(m3 - 10)
print(10 - m3)
print('-' * 80)
m4 = Matrix([[50.30, 12.06, 32.70, 38.09], [10.01, 23.5, 44.0, 6.9]])
print(m1 + m4)
print(m4 + m1)
print('-' * 80)
print(m1 - m4)
print(m4 - m1)
print('-' * 80)
print(m4 / 10)
print(10 / m4)
print('-' * 80)
print(m4 * 10)
print(10 * m4)
print('-' * 80)
m5 = Matrix([[0.0, 1.0, 2.0, 3.0],
            [0.0, 2.0, 4.0, 6.0]])
m6 = Matrix([[0.0, 1.0],
            [2.0, 3.0],
            [4.0, 5.0],
            [6.0, 7.0]])
print(m5 * m6)
print(m6 * m5)
print('-' * 80)
v1 = Vector([1.0, 2.0, 0.0, 1.0])
print(m1 * v1)
