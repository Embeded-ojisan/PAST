import sys

N = int(input())

A = []
B = []

for i in range(N):
    a = list(input())
    A.append(list(a))

for i in range(N):
    b = list(input())
    B.append(list(b))

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:

            moji = str(i+1) + " " + str(j+1)
            print(moji)
            sys.exit()

