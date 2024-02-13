N = int(input())
a = list(map(int, input().split()))

s = 0

for i in range(N):
    s += a[i]

x = s//N
r = s%N

b = [x]*N

for i in range(r):
    b[i] += 1

a.sort()
b.sort()

ans = 0

for i in range(N):
    ans += abs(a[i]-b[i])

print(ans//2)