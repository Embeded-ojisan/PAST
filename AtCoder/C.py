N ,K = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

ans = 10**9

if N-1 == K:
    print(0)
    exit()

for i in range(K+1):
    B = A[i:len(A)-(K-i)]
    ans = min(ans, A[len(A)-(K-i)-1]-A[i])

print(ans)
