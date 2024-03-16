# 文字列(配列)の配列の定義の仕方

H, W = list(map(int, input().split()))

S = [input() for _ in range(H)]

for i in range(H):
    moji = ""
    for j in range(W-1):
        if S[i][j] == 'T' and S[i][j+1] == 'T':
            S[i] = S[i][:j] + 'P' + S[i][j+1:]
            S[i] = S[i][:j+1] + 'C' + S[i][j+2:]
        moji += S[i][j]
    moji += S[i][W-1]
    print(moji)
