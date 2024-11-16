# 2次元座標での移動を表す辞書
directions = {
    "U": (0, -1),  # 上に移動 (y座標を-1)
    "D": (0, 1),   # 下に移動 (y座標を+1)
    "L": (-1, 0),  # 左に移動 (x座標を-1)
    "R": (1, 0)    # 右に移動 (x座標を+1)
}

# 使用例
current_position = (2, 2)
move = "U"
new_position = (current_position[0] + directions[move][0], current_position[1] + directions[move][1])

print("移動後の位置:", new_position)
