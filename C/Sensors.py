class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1]*(n+1)
        self.size = [1]*(n+1)

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)

        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)
    
H, W = list(map(int, input().split()))

S = []

for i in range(H):
    S.append(input())

n = H*W
ans = 0

dsu = unionfind(n)

for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        ans+=1
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni = i+di
                nj = j+dj
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if S[ni][nj] != '#':
                    continue
                if i == ni and j == nj:
                    continue
                v = i*W+j
                u = ni*W+nj
                if dsu.same(v, u) == True:
                    continue
                dus.unite(v, u)
                ans -= 1

print(str(ans))