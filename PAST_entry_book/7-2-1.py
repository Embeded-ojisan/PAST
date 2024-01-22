import bitsect

N, M = list(map(int, input().split()))
A = list(map(int, input()))

B = [0] * N

for a in A:
    k = bitsect.bitsect_right(B, -a)

    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a