class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n     # for union by rank
        # self.rank = [1] * n   # for union by size

    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)

        # Union by rank
        if par_a != par_b:
            if self.rank[par_a] > self.rank[par_b]:
                self.parent[par_b] = self.parent[par_a]
            elif self.rank[par_a] < self.rank[par_b]:
                self.parent[par_a] = self.parent[par_b]
            else:
                self.parent[par_b] = self.parent[par_a]
                self.rank[par_a] += 1

        # # Union by size
        # if par_a != par_b:
        #     if self.rank[par_a] < self.rank[par_b]:
        #         self.parent[par_a] = self.parent[par_b]
        #         self.rank[par_b] += self.rank[par_a]
        #     else:
        #         self.parent[par_b] = self.parent[par_a]
        #         self.rank[par_a] += self.rank[par_b]

    def find(self, a):
        if self.parent[a] != a:
            # Path compression/collapsing
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
