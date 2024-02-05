N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

S = []

for i in range(N):
    S.append(input())

now_sc = [0]*(N)

for i in range(0, N):
    now_sc[i] = i

for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            now_sc[i] += A[j]

mx = 0

for i in range(N):
    mx = max(mx, now_sc[i])

for i in range(N):
    nokori = []

    for j in range(M):
        if S[i][j] == 'x':
            nokori.append(A[j])

    nokori = sorted(nokori, reverse=True)

    ans = 0

    while now_sc[i] < mx:
        now_sc[i] += nokori[ans]
        ans += 1

    print(str(ans))

