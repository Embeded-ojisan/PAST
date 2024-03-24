import math
import sys

W, B = list(map(int, input().split()))

mihon = ""

for i in range(100):
    mihon += "w"+"b"

if W == 0:
    if B == 1:
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()
elif B == 0:
    if W == 1:
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()

baisuu = math.gcd(W, B)

Wb = W // baisuu
Bb = B // baisuu

moji = ""

if Wb > Bb:
    moji += "w"
    for i in range(Bb):
        moji += "bw"
elif Wb == Bb:
    print("Yes")
    sys.exit()
else:
    moji += "b"
    for i in range(Wb):
        moji += "wb"

if moji in mihon:
    print("Yes")
else:
    print("No")
