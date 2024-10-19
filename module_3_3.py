
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('a')
print_params(False, 'a')
print_params({4, 6, 7}, False, 'a')
print_params({4, 6, 8}, False, 'a')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'a2', False]
values_dict = {'a': 15, 'b': False, 'c': 'r7'}
values_list_2 = [True, 23]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
