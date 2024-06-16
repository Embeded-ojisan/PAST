import sys

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0

temp = 0
ai = 0
for i in range(M):
    while ai < N and A[ai] < B[i]:
        ai += 1
    if ai == N:
        print("-1")
        sys.exit()
    ans += A[ai]
    ai += 1

print(ans)