# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from typing import List
from ..disjoint_set_union import DSU


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        dsu = DSU(n)
        for i in range(n):
            for kid in adj[i]:
                dsu.union(i, kid)
        par = set()
        for i in range(n):
            par.add(dsu.find(i))
        return n - len(par)
