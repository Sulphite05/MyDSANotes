# https://www.geeksforgeeks.org/problems/number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-islands

from typing import List
from DSU.disjoint_set_union import DSU


class Solution:
    def numOfIslands(self, rows: int, cols: int, operators: List[List[int]]) -> List[int]:
        dsu = DSU(rows * cols)
        DIR = [0, 1, 0, -1, 0]
        ans = [1]
        op = [[0] * cols for _ in range(rows)]
        oper_x, oper_y = operators[0]
        op[oper_x][oper_y] = 1

        for a, b in operators[1:]:
            curr = 1
            p = cols * a + b
            if op[a][b]:
                ans.append(ans[-1])
                continue
            op[a][b] = 1
            for i in range(4):
                x, y = a + DIR[i], b + DIR[i + 1]
                n = cols * x + y
                if 0 <= x < rows and 0 <= y < cols and op[x][y]:
                    curr -= dsu.union(n, p)

            ans.append(ans[-1] + curr)
        return ans
