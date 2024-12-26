# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

from typing import List
from heapq import heappush, heappop
from ..disjoint_set_union import DSU


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:

        # Kruskal's algorithm
        final = []

        for i in range(V):
            for ch, weight in adj[i]:
                final.append([weight, i, ch])

        dsu = DSU(V)
        final.sort()
        ans = 0
        for w, p, c in final:
            if dsu.find(p) != dsu.find(c):
                ans += w
                dsu.union(p, c)
        return ans


        # Prims Algorithm
        summ = 0
        heap = [(0, 0)]
        vis = set()
        while heap:
            cost, curr = heappop(heap)
            if curr in vis: continue
            vis.add(curr)
            summ += cost
            for kid, cst in adj[curr]:
                heappush(heap, (cst, kid))
        return summ