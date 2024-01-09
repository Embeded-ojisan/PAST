K = int(input())

A, B = list(map(int, input().split()))

if A % K != 0 and B % K != 0 and (B//K - A//K)>0:
    print("OK")
elif A%K == 0 or B%K == 0:
    print("OK")
else:
    print("NG")