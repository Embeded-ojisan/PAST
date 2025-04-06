# A = [[False]*W for _ in range(H])]は間違い
A = [[False]*W for _ in range(H)]

A = [list(input()) for _ in range(N)]

# 以下はNG
A = [[] for _ in range(N)]
for i in range(N):
    a = list(input())
    A[i].append(a)