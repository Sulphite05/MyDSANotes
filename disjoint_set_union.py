class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

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

    def find(self, a):
        if self.parent[a] != a:
            # Path compression/collapsing
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


# NOTES
# Can be used for detecting cycles in a graph - Kruskal's algorithm(Minimum Spanning Tree)
# If two nodes belong to same set then they are is a cycle
# Can be used to check the number of connected graphs
# Requirements: Graph must be undirected

# Steps
# 1. Union
# 2. Find
# Using collapsing find, we can reduce time for finding the parent to
# nearly constant time or inverse Ackermann function
