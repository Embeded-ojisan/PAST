H = int(input("行数を入力してください: "))
S = []

print("各行の要素をスペース区切りで入力してください:")
for i in range(H):
    row = list(map(str, input().split()))
    S.append(row)

print("入力された二次元配列:")
for row in S:
    print(" ".join(row))