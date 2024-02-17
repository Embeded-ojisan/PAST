H, W = list(map(int, input().split()))

S = []

for i in range(H):
    S.append(input())

li = H
lj = W
ri = 0
rj = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            li = min(li, i)
            lj = min(lj, j)
            ri = max(ri, i)
            rj = max(rj, j)

moji = ""

for i in range(li, ri+1):
    for j in range(lj, rj+1):
        if S[i][j] == '.':
            moji = str(i+1) + ' ' + str(j+1)

print(moji)