import copy

# 元の配列
original_array = [[1, 2, 3], [4, 5, 6]]

# deepcopyを使って配列をコピー
copied_array = copy.deepcopy(original_array)

# 元の配列を変更して確認
original_array[0][0] = 99

# 出力
print("元の配列:", original_array)
print("コピーした配列:", copied_array)
