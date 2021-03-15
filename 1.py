l = [1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]


def print_list(l):
    for i in l:
        if type(i) == int:
            l2.append(i)
            print(i)
        else:
            print_list(i)


print_list(l)
