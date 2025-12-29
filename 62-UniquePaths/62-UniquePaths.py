# Last updated: 29/12/2025, 03:03:53
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
            Understand
                Inputs  - m (int): number of rows in a grid
                        n (int): number of columns in a grid
                Outputs - number of unique paths from top-left (0,0)
                        to bottom-right (m-1, n-1)
                Constraints - Only moves allowed: right or down
                            1 ≤ m, n ≤ 100 (typical limits)
                Examples / edge cases -
                    uniquePaths(3, 7) → 28
                    uniquePaths(1, 1) → 1 (only one cell)
                    uniquePaths(2, 2) → 2 (right→down or down→right)
                    uniquePaths(3, 2) → 3

            Plan
                HL: Use recursion + memoization (top-down DP)
                    - Treat grid as coordinates (i, j)
                    - Base case: top-left (0, 0) has exactly 1 path
                    - Out-of-bounds cells return 0
                    - Each cell (i, j) = paths from top + left:
                            path(i, j) = path(i-1, j) + path(i, j-1)
                    - Store computed results in memo to avoid repeats
                    - Return path(m-1, n-1)

            Time:  O(m * n)
                Each cell’s result is computed once due to memoization.
            Space: O(m * n)
                For recursion stack + memo dictionary.
        """


        memo = {(0,0) : 1}
        def path(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif i < 0 or j < 0 or i == m or j == n:
                return 0
            else:
                val = path(i, j-1) + path(i-1, j)
                memo[(i,j)] = val
                return val

        return path(m-1, n-1)
        