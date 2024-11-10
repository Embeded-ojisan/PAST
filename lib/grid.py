H = int(input("行数を入力してください: "))  # 行数を入力
S = []  # 二次元配列の初期化

print("各行の要素をスペース区切りで入力してください:")
for i in range(H):
    row = list(map(str, input().split()))  # 1行分をリストとして取得
    S.append(row)  # 二次元配列に追加

# 結果の表示（確認用）
print("入力された二次元配列:")
for row in S:
    print(" ".join(row))