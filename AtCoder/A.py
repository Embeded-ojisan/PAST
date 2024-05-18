import math

H = int(input())

ans = 0
length = 0

count = math.log2(H)

for i in range(0, 30):
    length += 2**i
    if length > H:
        ans = i + 1
        break

print(ans) 