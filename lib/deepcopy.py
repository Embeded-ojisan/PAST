import copy

original_array = [[1, 2, 3], [4, 5, 6]]

copied_array = copy.deepcopy(original_array)

original_array[0][0] = 99

print("元の配列:", original_array)
print("コピーした配列:", copied_array)
