def ft_filter(function_to_apply, list_of_inputs):
    return ([item for item in list_of_inputs if function_to_apply(item)])


numbers = [0, 1, 2, 3, 4]
print(list(filter(lambda x: bool(x % 2), numbers)))
print(list(ft_filter(lambda x: bool(x % 2), numbers)))
