import sys
from itertools import product
sys.setrecursionlimit(100)


def get_possible_moves(process_list, n):
    possible_change = []
    if process_list[0] == process_list[-1]:
        possible_change.append([0, (process_list[0] + 1) % (n + 1)])
    for ind in range(1, n):
        if process_list[ind] != process_list[ind - 1]:
            possible_change.append([ind, process_list[ind - 1]])
    return possible_change


def mutual_exclusion(process_list, steps):
    global result
    n = len(process_list)
    possible_change = get_possible_moves(process_list, n)
    print(possible_change)
    if len(possible_change) == 1:
        if result < steps:
            result = steps
    else:
        steps += 1
        for index, value in possible_change:
            new_process_list = process_list.copy()
            new_process_list[index] = value
            mutual_exclusion(new_process_list, steps)


result = 0
k = 5
how_many = k ** k
all_steps = []
help_array = []
steps = 0


for i, el in enumerate(product(range(k), repeat=k)):
    mutual_exclusion(list(el), steps)
print(result)