N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

wa = 0
ac = 10**9

while wa+1<ac:
    wj = (wa+ac)//2
    na = 0
    nb = 0
    for i in range(N):
        if A[i] <= wj:
            na += 1
    for i in range(M):
        if B[i] >= wj:
            nb += 1

    if na >= nb:
        ac = wj
    else:
        wa = wj

print(ac)