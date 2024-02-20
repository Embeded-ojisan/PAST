import itertools
import sys

N, M = list(map(int, input().split()))

S = []

for i in range(N):
    s = input()
    S.append(s)

ALL = list(itertools.permutations(S))

for a in ALL:
    ok = True
    for i in range(N-1):
        d = 0
        for j in range(M):
            if a[i][j] != a[i+1][j]:
                d += 1
        if d != 1:
            ok = False
    if ok == True:
        print("Yes")
        sys.exit()

print("No")