N = int(input())

A = list(map(int, input().split()))

def func(p, q):
    if q == 0:
        return
    if A[p] == A[q]:
        del A[q]
        A[p] += 1
        func(p-1, p)


i = 0
while i < len(A)-1:
    if A[i] == A[i+1]:
        A[i] += 1
        del A[i+1]
        func(i-1, i)
        i -= 1
        continue
    i += 1

print(len(A))
