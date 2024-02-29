import sys

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort(reverse=True)

result = False

for i in range(N):
    y = A[i]-X
    if A.count(y):
        print("Yes")
        sys.exit()

print("No")