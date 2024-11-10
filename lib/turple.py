# タプルの配列
tuple_array = [(3, 'apple'), (1, 'banana'), (4, 'cherry'), (2, 'date')]

# 1番目の要素をキーとしてソート
tuple_array.sort(key=lambda x: x[0])

# ソート結果を表示
print("ソート後:", tuple_array)