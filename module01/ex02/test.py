from vector import Vector


v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 16))
# print(v1.__dict__)
# print(v2.__dict__)
# print(v3.__dict__)
print(v3)
v4 = v2 + Vector([6.3, 7.1, 2.9])
print(v4)
v5 = v2 + 2.8
print(v5)
v6 = v1 - Vector((10, 14))
print(v6)
