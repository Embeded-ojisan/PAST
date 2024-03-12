T = input()
N = int(input())
M = len(T)

dp = [[1001001001]*(M+1)]*(N+1)

dp[0][0] = 0

for i in range(N):
    S = list(map(str, input().split()))
    A = int(S[0])
    
    for j in range(M+1):
        dp[i+1][j] = dp[i][j]
    
    for ai in range(A):
        l = len(S[ai+1])
        for j in range(M+1):
            if (j + l) > M:
                continue
            ok = True
            for k in range(l):
                if T[j+k] != S[ai+1][k]:
                    ok = False
            if ok==True:
                dp[i+1][j+l] = min(dp[i][j]+1, dp[i+1][j+l])

ans = dp[N][M]

if ans == 1001001001:
    ans = -1

print(ans)