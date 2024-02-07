import math

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

A.sort()

sum = [0]*(A[N-1]+1)

ans = 0
r = 0

for l in range(N):
    while r < n and a[r] < a[l]+m:
        r += 1
    ans = max(ans, r-l)

print(max)