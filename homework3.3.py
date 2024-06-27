def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 10, 'string']
values_dict = {'a': 'hello', 'b': True, 'c': 12}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [0.54, 'sky']
print_params(*values_list_2, 42)