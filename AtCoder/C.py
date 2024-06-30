def min_cost_to_replace_duplicates(A, W, N):
    from collections import Counter
    
    # 1からNまでの数値をセットとして用意
    full_set = set(range(1, N + 1))
    
    # 配列Aの要素の出現回数をカウント
    count_A = Counter(A)
    
    # 配列Aに含まれていない数値（欠けている数値）を特定
    missing = list(full_set - set(A))

    print(f"Missing numbers: {missing}")
    
    # 重複している数値とその対応するインデックスを分けて収集
    duplicates = {}
    for i, value in enumerate(A):
        if count_A[value] > 1:
            if value not in duplicates:
                duplicates[value] = []
            duplicates[value].append((W[i], i))

    # 出現回数が1回以上の重複要素を持つリストを作成し、重複ごとにソート
    sorted_duplicates = []
    for key in duplicates:
        sorted_duplicates.extend(sorted(duplicates[key]))

    print(f"Duplicates after sorting: {sorted_duplicates}")

    # 最小コストで重複を置き換える
    min_cost = 0
    replace_count = min(len(sorted_duplicates), len(missing))
    
    for i in range(replace_count):
        cost, index = sorted_duplicates[i]
        A[index] = missing[i]  # 重複要素を欠けている数値に置き換え
        min_cost += cost
    
    return min_cost

# 使用例
A = [2, 2, 3, 3, 5]
W = [10, 1, 3, 2, 5]
N = 6
result = min_cost_to_replace_duplicates(A, W, N)
print(result)  # 出力例: 3



N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

ans = min_cost_to_replace_duplicates(A, W, N)
print(ans)