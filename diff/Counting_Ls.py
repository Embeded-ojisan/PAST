N = int(input())

S = []

for i in range(N):
    S.append(input())

r = [0]*N
c = [0]*N

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            r[i] += 1
            c[j] += 1

ans = 0

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            ans += (r[i]-1)*(c[j]-1)

print(ans)
