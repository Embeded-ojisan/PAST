N, X, Y, Z = list(map(int, input().split()))

if X <= Z and Z <= Y:
    print("Yes")
elif Y <= Z and Z <= X:
    print("Yes")
else:
    print("No")