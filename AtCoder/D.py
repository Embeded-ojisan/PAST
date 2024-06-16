import sys

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0

temp = 0
for i in range(M):
    if temp > N -1:
        print("-1")
        sys.exit()
    for j in range(temp, N):
        if A[j] >= B[i]:
            ans += A[j]
            temp = j+1
            break
        elif j >= N-1 and i < M-1:
            print("-1")
            sys.exit()

print(ans)