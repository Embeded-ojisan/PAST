N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = [0]*(N+1)

past = 0

for i in range(M-1, 0, -1):
    past = 0
    for j in range(A[i], A[i-1], -1):
        B[j] = past
        past += 1

past = 0
for i in range(A[0], 0, -1):
    B[i] = past
    past += 1

for i in range(1, N+1):
    print(str(B[i]))