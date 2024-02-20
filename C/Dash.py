import sys

N, M, H, K = list(map(int, input().split()))
                  
S = input()

X = []
Y = []

s = set()

for i in range(M):
    x, y = list(map(int, input().split()))
    s.add((x, y))

x = 0
y = 0


for i in range(N):
    if S[i] == 'R':
        x += 1
    if S[i] == 'L':
        x -= 1
    if S[i] == 'U':
        y += 1
    if S[i] == 'D':
        y -= 1

    H -= 1
    if H < 0:
        print(s)
        sys.exit()
    if (x, y) in s:
        if H < K:
            H = K
            s.discard((x, y))


print("Yes")

