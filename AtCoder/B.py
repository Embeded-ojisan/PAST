N = int(input())

d = []

total = 0

for i in range(N):
    s, c = list(input().split())

    c = int(c)

    total += c

    d.append((s, c))

d.sort(key=lambda x: x[0])

ans = total % N

print(d[ans][0])

