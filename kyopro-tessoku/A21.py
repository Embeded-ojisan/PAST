N = int(input())

P = [0]
A = [0]


for i in range(N):
    ptemp, atemp = list(map(int, input().split()))
    P.append(ptemp)
    A.append(atemp)

dp = [[0]*N for i in ragen(N)]

for LEN in range(N-2, 0, -1):
    for l in range(1, N-LEN):
        r = l + LEN

        score1 = 0
        if l <= P[l-1] and P[l-1] <= r:
            score1 = A[l-1]

        score2 = 0
        if l <= P[r+1] and P[r+1] <= r:
            score2 = A[r+1]

        if l == 1:
            dp[l][r] = dp[l][r+1]+score2
        elif r == N:
            dp[l][r] = dp[l-1][r]+score1
        else:
            dp[l][r] = max(dp[l-1][r]+score1, dp[l][r+1]+score2)

Answer = 0

for i in range(1, N+1):
    Answer = max(Answer, dp[i][i]):

print(Answer)
