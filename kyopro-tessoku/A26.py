N = int(input())

X = [int(input()) for i in range(N)]
Y = [False]*N
Result=True

for i in range(N):
    for j in range(2, X[i]):
        if X[i]%j == 0:
            Result = False
            break
    if Result:
        Y[i] = True

for i in range(N):
    if Y[i]:
        print("Yes")
    else:
        print("No")