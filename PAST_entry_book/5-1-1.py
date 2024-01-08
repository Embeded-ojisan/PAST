# 前処理
A = [0, 0, 0] * 3
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Result = "No"

# ビンゴカードを取り込む
for i in range(3):
    A[i] = list(map(int, input().split()))

# 印を付ける
N = int(input())
for n in range(N):
    b = int(input())

    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                B[i][j] = 1
                break

# ビンゴがあるかをチェックする
## 縦チェック
if (B[0][0] and B[1][0] and B[2][0]) \
    or (B[0][1] and B[1][1] and B[2][1]) \
    or (B[0][2] and B[1][2] and B[2][2]):
        Result = "Yes"

## 横チェック
if (B[0][0] and B[0][1] and B[0][2]) \
    or (B[1][0] and B[1][1] and B[1][2]) \
    or (B[2][0] and B[2][1] and B[2][2]):
        Result = "Yes"

## 斜めチェック
if (B[0][0] and B[1][1] and B[2][2]) \
    or (B[0][2] and B[1][1] and B[2][0]):
        Result = "Yes"

print(Result)