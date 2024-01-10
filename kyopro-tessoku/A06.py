N, Q = list(map(int, input().split()))
            
A = []
S = []

S.append(0)

A = list(map(int, input().split()))

for i in range(N):
    S.append(S[i] + A[i])

for i in range(Q):
    L, R = list(map(int, input().split()))
    print(str(S[R]-S[L-1]))
