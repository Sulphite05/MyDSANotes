class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i <= j:
                    dp[i][j] = max(price[i - 1] + dp[i][j - i], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][n]


# We need to take care that all possibilities could be taken care of
# over and over again which is not possible in recursion.
# Not just the current one. If we have taken a certain element then
# it can be used again anytime in the future.
