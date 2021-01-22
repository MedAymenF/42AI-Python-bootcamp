from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    if (len(list_of_inputs) == 1):
        return list_of_inputs[0]
    return function_to_apply(list_of_inputs[0],
                             ft_reduce(function_to_apply, list_of_inputs[1:]))


lst = [12, 98, 23, 0, 44, 30, 56]
print(reduce(lambda x, y: max(x, y), lst))
print(ft_reduce(lambda x, y: max(x, y), lst))
