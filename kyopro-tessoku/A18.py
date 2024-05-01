N, S = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

dp = [[False]*10009]*69

dp[0][0] = True

for i in range(N+1):
    for j in range(S+1):
        if j < A[i]:
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if j >= A[i]:
            if dp[i-1][j] == True or dp[i-1][j-A[i]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S] == True:
    print("Yes")
else:
    print("No")