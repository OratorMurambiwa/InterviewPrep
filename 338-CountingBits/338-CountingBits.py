# Last updated: 29/12/2025, 03:03:08
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
            Understand
                Inputs - integer n
                Outputs - list dp where dp[i] = count of 1-bits in i
                Constraints - 0 ≤ n ≤ 10^5
                Edge cases - n = 0

            Plan
                HL:
                1. Initialize dp array of zeros (size n+1).
                2. Initialize offset = 1 (first power of two).
                3. For each number i from 1..n:
                - If i == offset * 2, update offset to i.
                - Set dp[i] = 1 + dp[i - offset]
                    (add one for the highest power-of-two bit).
                4. Return dp.

            Time: O(n) — single pass.
            Space: O(n) — for the dp list.
        """

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
        