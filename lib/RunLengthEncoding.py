def run_length_encoding(array):
    if not array:
        return []

    compressed = [] 
    current_value = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = array[i]
            count = 1

    compressed.append((current_value, count))
    return compressed

array = [1, 1, 2, 2, 2, 3, 3, 1, 1, 1]
compressed_array = run_length_encoding(array)
print("ランレングス圧縮結果:", compressed_array)
