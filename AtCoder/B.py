import sys

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

X=[0]*M

for i in range(N):
    x = list(map(int, input().split()))
    for j in range(M):
        X[j] += x[j]

for i in range(M):
    if X[i] < A[i]:
        print("No")
        sys.exit()
print("Yes")