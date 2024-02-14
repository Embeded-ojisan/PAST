import sys

N, K = list(map(int, input().split()))

ps = {}

total = 0

for i in range(N):
    a, b = list(map(int, input().split()))
    ps[a] = b
    total += b

if total <= K:
    print("0")
    sys.exit()

ps1 = sorted(ps.items())

for a, b in ps1:
    total -= b
    if total <= K:
        print(str(a+1))
        sys.exit()

print(0)