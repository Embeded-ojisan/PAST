N, W = list(map(int, input().split()))

ws = [0]
vs = [0]

for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

values = []
for i in range(N+1):
    values.append([-10**18]*(W+1))

values[0][0] = 0

for i in range(1, N+1):
    for w in range(1, N+1):
        values[i][w] = max(values[i][w], values[i-1][w])

        if w-ws[i] >= 0:
            values[i][w] = max(values[i][w], values[i-1][w-ws[i]] + vs[i])

ans = max(values[N])
print(ans)