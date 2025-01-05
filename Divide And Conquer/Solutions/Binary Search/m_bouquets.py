# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        n = len(bloomDay)

        def feasible(days):
            bouquets = flowers = 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bouquets >= m

        if n < m * k: return -1

        st, en = 1, max(bloomDay)
        while st < en:
            mid = st + (en - st) // 2
            if feasible(mid):
                en = mid
            else:
                st = mid + 1
        return st
