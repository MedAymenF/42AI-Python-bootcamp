import numpy as np


class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)


npc = NumPyCreator()

print(npc.from_list([[1, 2, 3], [6, 3, 4]]).__repr__())

print(npc.from_tuple(("a", "b", "c")).__repr__())

print(npc.from_iterable(range(5)).__repr__())

shape = (3, 5)
print(npc.from_shape(shape).__repr__())

print(npc.random(shape).__repr__())

print(npc.identity(4).__repr__())
