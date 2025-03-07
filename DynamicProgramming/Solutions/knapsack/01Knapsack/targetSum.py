# https://leetcode.com/problems/target-sum/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sum(S1) - sum(S2) = diff
        # sum(S1) + sum(S2) = sum(arr)
        # 2*sum(S1) = diff + sum(arr)
        # sum(S1) = (diff + sum(arr))/2
        sum_num = sum(nums)
        if sum_num < abs(target): return 0
        summ = (target + sum_num)
        if summ & 1: return 0
        summ >>= 1

        # Rest is simple DP
        n = len(nums)
        dp = [[1] + [0] * summ for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(0, summ + 1):
                # starting with sum 0 here because there are 2 ways to do it here as well +0, -0 while taking elements 0
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][summ]

