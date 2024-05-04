N = int(input())

A = []

for i in range(N):
    atemp, btemp = list(map(int, input().split()))
    A.append((atemp, btemp, btemp-atemp))

A.sort(key=lambda x: x[2])

length = 0

for i in range(N-1):
    length += A[i][0]
length += A[N-1][1]

print(length)