import sys

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))


# Aをsort
A.sort()

# Aの中の値が2つ連続しているかを検査

n = len(A)

if n < 2:
    print("No")
else:
    for i in range(n):
        if A[i] + 1 == A[i+1]:
            print("Yes")
            sys.exit()
    print("No")