def Power(a, b, m):
    p = a
    Answer = 1

    for i in range(30):
        wari = 2**i

        if (b//wari) % 2 == 1:
            Answer = (Answer * p) % m
        p = (p * p) % m
    return Answer

def Division(a, b, m):
    return (a * Power(b, m - 2, m)) % m

H, W = map(int, input().split())
M = 1000000007

a = 1
for i in range(1, H):
    a = (a * i) % M

b = 1
for i in range(1, W):
    b = (b * i) % M

for i in range(1, H+W-1):
    b = (b * i) % M

print(Division(a, b, M))