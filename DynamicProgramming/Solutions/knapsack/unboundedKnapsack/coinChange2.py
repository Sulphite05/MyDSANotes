# https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[1] + [0] * amount for _ in range(n+1)]
        for i in range(1, n+1): # coin
            for j in range(1, amount + 1): # curr sum
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]