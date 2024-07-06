N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A.insert(K, X)

ans = ""

for a in A:
    ans += str(a) + " "
print(ans)