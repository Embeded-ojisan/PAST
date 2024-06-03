N, M = list(map(int, input().split()))

N += 1

ans = 0

for i in range(60):
    if (M >> i) & 1:
        p = 2 << i
        r = N % p
        ans += ((N-r)//2)

        if r >= (1<<i):
            ans += (r-(1<<i))

print(ans%998244353)