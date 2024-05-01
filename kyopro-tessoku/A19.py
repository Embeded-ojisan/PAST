N, W = list(map(int, input().split()))

w = [0]
v = [0]

# dp = [[-1000000000]*(W+1)]*(N+1)

dp = [[-10000]*(W+1) for i in range(N+1)]

for i in range(1, N+1):
    wtemp, vtemp = list(map(int, input().split()))
    w.append(wtemp)
    v.append(vtemp)


dp[0][1] = 77

for i in range(N+1):
    dp[i][0] = 0

for j in range(W+1):
    dp[0][j] = 0

for i in range(1, N+1):
    print(dp)
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+ v[i])

Answer = 0

for i in range(W+1):
    Answer = max(Answer, dp[N][i])

print(w)
print(v)
print(dp[N])
print(Answer)
