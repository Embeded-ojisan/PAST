import copy

N = int(input())
A = list(map(int, input().split()))

M = 1000004

is = [0]*M

for i in range(N):
    is[a[i]].append(i)

ans = [0]*N

now = 0

for x in range(M-1, 0, -1):
    for i in is[x]:
        ans[i] = now
    now += x*len(is[x])

moji = ""

for i in range(N):
    moji += str(ans[i]) + " "

print(moji)