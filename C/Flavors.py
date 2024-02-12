N = int(input())

a = [[] for _ in range(N)]

for i in range(N):
    f, s = list(map(int, input().split()))
    f = int(f)

    a[f-1].append(s)

ans = 0

for i in range(N):
    a[i].sort(reverse=True)
    if len(a[i]) < 2:
        continue
    now = a[i][0] + a[i][1]//2
    ans = max(ans, now)

b = []

for i in range(N):
    if len(a[i]) == 0:
        continue
    b.append(a[i][0])

b.sort(reverse=True)

if len(b) >= 2:
    ans = max(ans, b[0]+b[1])

print(ans)