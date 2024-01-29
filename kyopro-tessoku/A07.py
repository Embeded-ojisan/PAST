D = int(input())
N = int(input())

S = [0] * (D+1)

for i in range(N):
    L, R = list(map(int, input().split()))
    for j in range(L, R+1):
        S[j] += 1

print(str(S[1]))

for i in range(2, D+1):
    S[i] += S[i-1]
    print(str(S[i] - S[i-1]))