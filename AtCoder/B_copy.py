import math
import sys
import itertools

W, B = list(map(int, input().split()))

mihon  = "wbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbwwbwbwwbwbwbw"

if W > 7 and B > 5:
    w = W%7
    b = B%5
elif (W > 7 and B <= 5) or (W <= 7 and B > 5):
    print("No")
    sys.exit() 
else:
    w = W
    b = B

A = ["w"]*w + ["b"]*b

ALL = list(itertools.permutations(A))

for a in ALL:
    moji = "".join(a)
    if moji in mihon:
        print("Yes")
        sys.exit()

print("No")
