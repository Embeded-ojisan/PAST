A, B, X = list(map(int,input().split()))

ng = 10**9+1
ok = 1

while abs(ok-ng)>1:
    M = (ok+ng)//2
    if (A*M + B*len(str(M)))<=X:
        ok = M
    else:
        ng = M

if ok <= 0:
    print("0")
else:
    print(str(ok))