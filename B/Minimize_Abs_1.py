N, L, R = list(map(int, input().split()))
A = list(map(int, input().split()))

moji = ""

for i in range(N):
    if A[i] >= L and R >= A[i]:
        moji += str(A[i]) + ' '
    elif A[i] <= L:
        moji += str(L) + ' '
    elif A[i] >= R:
        moji += str(R) + ' '

print(moji)