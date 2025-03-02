# https://leetcode.com/problems/partition-equal-subset-sum/

from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2: return False
        val = total >> 1

        # We'll find one subset with this sum. If it's there, we're done :)

        # # Recursive DP
        @lru_cache(None)
        def part(i, summ):
            if not summ: return True
            if i == n: return False
            get = False
            if summ - nums[i] >= 0:
                get = part(i + 1, summ - nums[i])  # use curr num
            return get if get else part(i + 1, summ)  # don't use curr num

        return part(0, val)

        # # Iterative DP
        dp = [[True] + ([False] * (val)) for _ in range(n + 1)]
        # if sum is 0, so no matter how many elements we have, we can create sum
        # by not using any element at all, so first column is True
        # But first row is False because we cannot make a sum > 0 with 0 elements

        for i in range(1, n + 1):
            for j in range(1, val + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][val]




