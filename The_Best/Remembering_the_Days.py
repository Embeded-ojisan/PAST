# 重み付き無向グラフの最長経路問題

N, M = list(map(int, input().split()))

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

g = [[] for _ in range(N)]

for i in range(M):
    a, b, c = list(map(int, input().split()))
    g[a-1].append(Edge(to=b-1, cost=c))
    g[b-1].append(Edge(to=a-1, cost=c))

ans = 0

visited = [False]*N

def f(v, dist):
    global ans
    visited[v] = True
    ans = max(ans, dist)
    for e in g[v]:
        if visited[e.to] == True:
            continue
        f(e.to, dist+e.cost)
    visited[v] = False

for i in range(N):
    f(i, 0)

print(ans)