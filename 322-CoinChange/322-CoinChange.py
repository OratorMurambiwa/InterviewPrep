# Last updated: 29/12/2025, 03:03:11
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        Understand
            Inputs  - coins: List[int], amount: int
            Outputs - int (minimum number of coins needed to make up amount)
            Constraints - You may use a coin as many times as you want
                        - If no combination can form the amount, return -1
                        - All coins are positive integers
            Examples/edge cases - coins = [1,2,5], amount = 11 → 3 (5+5+1)
                                - coins = [2], amount = 3 → -1
                                - coins = [1], amount = 0 → 0
                                - coins = [], amount = 7 → -1

        Plan 
            HL: Use bottom-up dynamic programming.
                - Create a dp array where dp[i] = fewest coins needed for amount i
                - Initialize dp[0] = 0 (0 coins needed to make amount 0)
                - Fill rest with a large placeholder (INF)
                - For each coin, try to update all values from coin to amount
                - Return dp[amount] if it has a valid value, else -1

        Time: O(n * m) where n = amount, m = number of coin types
        Space: O(n) for the dp array
        """

        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)

        if dp[amount] == INF:
            return -1
        else:
            return dp[amount]




        