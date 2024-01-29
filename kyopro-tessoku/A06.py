N, Q = list(map(int, input().split()))

A = [0] + list(map(int, input().split()))
S = [0] * (N+1)

for i in range(1, N+1):
    S[i] = S[i-1] + A[i]

for i in range(Q):
    l, r = list(map(int, input().split()))
    print(str(S[r] - S[l-1]))

