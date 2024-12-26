# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from typing import List
from ..disjoint_set_union import DSU


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1

        dsu = DSU(n)

        for a, b in connections:
            dsu.union(a, b)

        pars = set()

        for i in range(n):
            pars.add(dsu.find(i))

        return len(pars) - 1
