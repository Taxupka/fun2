

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

valve_list = [545, True, 'fafa']
valve_dict = {'a': 'dada', 'b': False, 'c': 335}
valve_list_2 = ['рампампам', 233]
print_params(b=25)
print_params(c=[1,2,3])
print_params(**valve_dict)
print_params()
print_params(*valve_list)
print_params(*valve_list_2, 42)

