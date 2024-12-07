H = int(input())
S = []

print("各行の要素をスペース区切りで入力してください:")
for i in range(H):
    row = input().strip()
    S.append(list(row))

print("入力された二次元配列:")
for row in S:
    print(" ".join(row))