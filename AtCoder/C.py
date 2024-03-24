N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

SUMV = K*(K+1)//2

A.sort()
if A[0] <= K:
    SUMA = A[0]
else:
    SUMA = 0

for i in range(1, N):
    if A[i] <= K and A[i] != A[i-1]:
        SUMA += A[i]

kotae = SUMV-SUMA

print(kotae)