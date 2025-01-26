# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        st = 0
        en = m * n - 1

        while st <= en:
            mid = (st + en) // 2
            r = mid // n
            c = mid - n * r
            val = matrix[r][c]
            if val == target:
                return True
            elif val < target:
                st = mid + 1
            else:
                en = mid - 1
        return False
