import sys
INF = 1<<30

n, k = map(int, input().split())
a = list(map(int, input().split()))

pre = [0] * (k+1)
suf = [0] * (k+1)

for i in range(1, k+1):
    pre[i] = pre[i-1]
    if i % 2 == 0:
        pre[i] += a[i-1] - a[i-2]

for i in range(k-1, -1, -1):
    suf[i] = suf[i+1]
    if (k-i)%2==0:
        suf[i] += a[i+1]-a[i]

ans = 10**9

for i in range(0, k+1, 2):
    ans = min(ans, pre[i]+suf[i])

print(str(ans))