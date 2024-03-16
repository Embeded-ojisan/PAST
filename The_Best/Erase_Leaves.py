# 深さ優先探索用の木構造の初期化のサンプル

import sys

sys.setrecursionlimit(100000)

n = int(input())

# ここを間違えるとうまく木構造が作れない
to = [[] for _ in range(n)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    to[a-1].append(b-1)
    to[b-1].append(a-1)

ans = n

def f(v, p):
    res = 1
    for u in to[v]:
        if u == p:
            continue
        res += f(u, v)
    return res

for v in to[0]:
    now = n-f(v, 0)
    ans = min(ans, now)

print(str(ans))