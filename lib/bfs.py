import sys
input = sys.stdin.readline

from collections import deque

H, W, D = list(map(int, input().split()))
S = []

for i in range(H):
    row = input().strip()
    S.append(list(row))

Z = []

visted = [[False]*W for _ in range(H)]

ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            Z.append((i, j))
            visted[i][j] = True

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def cnt(x, y, val):
    # 仮引数の値をmove(グローバルな変数)ととしない
    visted[x][y] = True
    queue = deque([x, y])

    while queue:
        x1, y1 = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0 <= nx < H and 0 <= ny < W and not temp[nx][ny] and (S[nx][ny] == ".") and val <= D:
                val += 1
                visted[nx][ny] = True
                queue.append((nx, ny))

for x, y in Z:
    move = 0
    cnt(x, y, move)

for i in range(H):
    for j in range(W):
        if visted[i][j] == True:
            ans += 1

print(ans)