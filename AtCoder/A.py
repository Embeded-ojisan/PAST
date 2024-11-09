import bisect

N, M, P = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Asum = [0] * N
Bsum = [0] * N

A.sort()
B.sort()

Asum[0] = A[0]
Bsum[0] = B[0]
for i in range(1, N):
    Asum[i] = Asum[i-1] + A[i]
    Bsum[i] = Bsum[i-1] + B[i]

ans = 0
for i in range(N):
    val = P - A[i]
    if val > B[0]:
        pos = bisect.bisect_left(B, val)
        ans += Bsum[pos-1] + A[i]*(pos) + P*(N-pos)
    else:
        ans += P*M
print(ans)
