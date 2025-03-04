# https://leetcode.com/problems/last-stone-weight-ii/
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Like Minimum subset sum difference
        # Range of sum is between 0 and sum of array
        n = len(stones)
        rng = sum(stones)
        # Final result is (rng - s) - s
        # or rng - 2s
        # so we need to find a subset in given array such that
        # s minimises the half distance to rng

        dp = [[True] + [False] * (rng) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, rng + 1):
                if stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - stones[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # Last row holds all the possible subset sums to get sum
        # We need to find the largest one
        for i in range(len(dp[-1]) >> 1, -1, -1):
            if dp[-1][i] and rng >= (i << 1): return rng - (i << 1)


# Space optimised
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Like Minimum subset sum difference
        # Range of sum is between 0 and sum of array
        n = len(stones)
        rng = sum(stones)
        # Final result is (rng - s) - s
        # or rng - 2s
        # so we need to find a subset in given array such that
        # s minimises the half distance to rng
        dp = [True] + [False] * (rng)
        for i in range(1, n + 1):
            curr = [True] + [False] * (rng)
            for j in range(1, rng + 1):
                if stones[i - 1] <= j:
                    curr[j] = dp[j - stones[i - 1]] or dp[j]
                else:
                    curr[j] = dp[j]
            dp = curr
        # Last row holds all the possible subset sums to get sum
        # We need to find the largest
        for i in range(len(dp) >> 1, -1, -1):
            if dp[i] and rng >= (i << 1): return rng - (i << 1)


# To count number of subsets with given difference
# sum(S1) - sum(S2) = diff
# sum(S1) + sum(S2) = sum(arr)
# 2*sum(S1) = diff + sum(arr)
# sum(S1) = (diff + sum(arr))/2
# sum(s1) is in decimal, we return 0
# else solve as above
