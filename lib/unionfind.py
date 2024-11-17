class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

n = 5
uf = UnionFind(n)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print("0と2は同じ集合に属するか:", uf.find(0) == uf.find(2))  # True
print("0と4は同じ集合に属するか:", uf.find(0) == uf.find(4))  # False
