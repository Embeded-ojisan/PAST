directions = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

current_position = (2, 2)
move = "U"
new_position = (current_position[0] + directions[move][0], current_position[1] + directions[move][1])

print("移動後の位置:", new_position)
