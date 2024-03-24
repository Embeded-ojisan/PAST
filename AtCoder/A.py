N = int(input())
A = list(map(int, input().split()))

moji = ""

for i in range(N-1):
    moji += str(A[i]*A[i+1]) + " "

print(moji)