N, M = list(map(int, input().split()))
S = input()

C = list(map(int, input().split()))

ps = [[] for _ in range(M)]

for i in range(N):
    ps[C[i]-1].append(i)

s = list(S)
ans = s.copy()

for i in range(M):
    l = len(ps[i])

    for j in range(l):
        x = (j+1)%l
        a = ps[i][x]
        b = ps[i][j]
        ans[a] = s[b]

ans_s = "".join(ans)
print(ans_s)