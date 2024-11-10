class UnionFind:
    def __init__(self, n):
        # 親を自分自身に初期化
        self.parent = [i for i in range(n)]
        # 各ノードのランクを0で初期化
        self.rank = [0] * n

    # 親を見つける（経路圧縮付き）
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    # Union by Rankによる連結
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # ランクの高い方を親にする
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                # ランクが同じ場合は一方を他方の親にし、ランクを1増やす
                self.parent[root2] = root1
                self.rank[root1] += 1

# 使用例
n = 5  # ノード数
uf = UnionFind(n)

# ノードを連結する
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

# 連結状態を確認
print("0と2は同じ集合に属するか:", uf.find(0) == uf.find(2))  # True
print("0と4は同じ集合に属するか:", uf.find(0) == uf.find(4))  # False
