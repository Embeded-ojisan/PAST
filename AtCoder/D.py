N, K = list(map(int, input().split()))

P = list(map(int, input().split()))

PP = []

for i in range(N):
    PP.append((i, P[i]))

PP.sort(key=lambda x: x[1])

ans = 20000000000

for i in range(N-K+1):
    tempmin = 200000000
    tempmax = 0
    for j in range(i, i+K):
        tempmin = min(tempmin, PP[j][0])
        tempmax = max(tempmax, PP[j][0])
    ans = min(ans, tempmax-tempmin)

print(ans)