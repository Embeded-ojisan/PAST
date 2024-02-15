N, S, M, L = list(map(int, input().split()))

ans = 1001001001

for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if i*6+j*8+k*12 < N:
                continue
            cost = i*S + j*M + k*L
            ans = min(ans, cost)

print(ans)





