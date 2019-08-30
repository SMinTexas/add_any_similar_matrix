# Using the solution from add_matrix.py, extend it to work for a pair of
# matrices of any size, as long as they have the same size.

first_list = [[1, 3], [2, 4]]
second_list = [[5, 2], [1, 0]]

result = [[], []]

for index, item in enumerate(first_list):
    for nested_index, nested_item in enumerate(item):
        result[index].append(first_list[index][nested_index] +
        second_list[index][nested_index])

print(result)

first_list = [[6, 1, 5], [3, 8, 7]]
second_list = [[2, 4, 2], [3, 9, 6]]

result = [[], []]

for index, item in enumerate(first_list):
    for nested_index, nested_item in enumerate(item):
        result[index].append(first_list[index][nested_index] +
        second_list[index][nested_index])

print(result)

first_list = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
second_list = [[11, 13, 15, 17, 19], [12, 14, 16, 18, 20]]

result = [[], []]

for index, item in enumerate(first_list):
    for nested_index, nested_item in enumerate(item):
        result[index].append(first_list[index][nested_index] +
        second_list[index][nested_index])

print(result)