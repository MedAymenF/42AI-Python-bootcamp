def ft_map(function_to_apply, list_of_inputs):
    return ([function_to_apply(item) for item in list_of_inputs])


numbers = [0, 1, 2, 3, 4]
print(list(map(lambda x: x * x, numbers)))
print(ft_map(lambda x: x * x, numbers))
