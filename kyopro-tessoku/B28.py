N = int(input())

A = [0] * N
A[0] = 1
A[1] = 1

for i in range(2, N):
    A[i] = A[i-1] + A[i-2]
    A[i] %= 1000000007

print(str(A[N-1]))