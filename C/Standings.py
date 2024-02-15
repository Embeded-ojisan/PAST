from functools import cmp_to_key

N = int(input())

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(a+b)

ans = [0] * N

for i in range(N):
    ans[i] = i

def cmp(a, b):
    if a==b:
        return 0
    return -1 if a < b else 1

def func(i, j):
    return cmp(A[i]*B[j], A[j]*B[i])

ans = sorted(ans, reverse=True ,key=cmp_to_key(func))

moji = ""

for i in range(N):
    moji += str(ans[i]+1) + ' '

print(moji)