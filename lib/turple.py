tuple_array = [(3, 'apple'), (1, 'banana'), (4, 'cherry'), (2, 'date')]

tuple_array.sort(key=lambda x: x[0])

print("ソート後:", tuple_array)