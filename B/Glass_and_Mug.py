K, G, M = list(map(int, input().split()))

g = 0
m = 0

k = 0

while k < K:
    k+=1
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        x = min(G-g, m)
        g += x
        m -= x

moji = str(g) + ' ' + str(m)

print(moji)