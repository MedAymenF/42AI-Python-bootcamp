from vector import Vector


v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 16))
print(v3)
v4 = v2 + Vector([6.3, 7.1, 2.9])
print(v4)
v5 = v2 + 2.8
print(v5)
print(2.8 + v2)
v6 = v1 - Vector((10, 14))
print(v6)
print(2 - v1)
print(v1 * 5)
print(5 * v1)
print(v1 * v1)
print(v3 * Vector((20, 26)))
print(Vector((20, 26)) * v3)
print(v2 / 0.1)
print(2 / v3)
