# Last updated: 01/01/2026, 04:44:07
1class Solution(object):
2    def coinChange(self, coins, amount):
3        """
4        :type coins: List[int]
5        :type amount: int
6        :rtype: int
7        """
8        dp = [0] * (amount+1)
9        coins.sort()
10
11        for i in range(1, amount + 1):
12            minn = float('inf')
13
14            for coin in coins:
15                diff = i - coin
16
17                if diff < 0:
18                    break
19                minn = min(minn, dp[diff] + 1)
20
21            dp[i] = minn
22
23        if dp[amount] < float('inf'):
24            return dp[amount]
25        else:
26            return -1
27        