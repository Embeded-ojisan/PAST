import math
N = int(intput())

x = math.ceil(N/9)

y = N%9

if y == 0:
    y = 9

ans = ""

for _ in range(0, 9):
    ans += str(y)

print(ans)