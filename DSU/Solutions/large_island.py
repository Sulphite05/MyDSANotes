# https://leetcode.com/problems/making-a-large-island/

from typing import List
from DSU.disjoint_set_union import DSU


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n*n)
        DIR = [0,1,0,-1,0]

        for i in range(n):
            for j in range(n):
                 if grid[i][j] == 1:
                    for d in range(4):
                        x, y = i + DIR[d], j + DIR[d+1]
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            dsu.union(n*i + j, n*x + y)

        final = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    ans = 1
                    for d in range(4):
                        x, y = i + DIR[d], j + DIR[d+1]
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            par = dsu.find(n*x + y)
                            if par not in seen:
                                seen.add(par)
                                ans += dsu.rank[par]
                    final = max(final, ans)
        return final if final else n*n
