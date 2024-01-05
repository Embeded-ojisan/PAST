N,Y = map(int, input().split())

ares, bres, cres = -1, -1, -1

for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if a+b+c == N and 10000*a + 5000*b + 1000*C == Y:
                ares, bres, cres = a, b, c

print(ares, bres, cres)