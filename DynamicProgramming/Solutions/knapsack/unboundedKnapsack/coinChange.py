# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0] = [float('inf')-1] * (amount + 1)
        # We cannot make the required sum with 0 coins so infinite coins is the case here
        # We do -1 to prevent overflow when we are adding 1 below
        dp[0][0] = 0    # However, We can create an amount of 0 by not using any coin at all
        for i in range(1, n + 1):  # coin
            for j in range(1, amount + 1):  # curr sum
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount] if dp[n][amount] != float('inf') else -1
