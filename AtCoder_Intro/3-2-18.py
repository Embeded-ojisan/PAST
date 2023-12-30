H, A = map(int, input().split())

X = H/A
Y = H%A

if Y > 0:
    print(A+1)
elif Y == 0:
    print(A)
else:
    print(0)