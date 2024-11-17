data_structure = [
   [1, 2, 3],
   {'a': 4, 'b': 5},
   (6, {'cube': 7, 'drum': 8}),
   "Hello",
   ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    mylist = list(data_structure)
    while len(mylist) > 1:
        k = 0
        x = 0
        a = []
        new_stru = []
        while k < len(mylist):
            if isinstance(mylist[k], str):
                if mylist[k].isdigit():
                    x = x + int(mylist[k])
                else:
                    x = x + len(mylist[k])
                k += 1
            elif isinstance(mylist[k], tuple):
                new_stru.append(list(mylist[k]))
                k += 1
            elif isinstance(mylist[k], set):
                new_stru.append(list(mylist[k]))
                k += 1
            elif isinstance(mylist[k], dict):
                new_stru.append(list(mylist[k].keys()))
                new_stru.append(list(mylist[k].values()))
                k += 1
            elif isinstance(mylist[k], list):
                new_stru.append(mylist[k])
                k += 1
            else:
                x = x + mylist[k]
                k += 1
        [[a.append(j) for j in i] for i in new_stru]
        mylist = a
        mylist.append(x)
    return x


result = calculate_structure_sum(data_structure)
print(result)
