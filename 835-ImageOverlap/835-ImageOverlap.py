# Last updated: 19/01/2026, 15:37:23
1class Solution(object):
2    def countSquares(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: int
6        """
7        m, n = len(matrix), len(matrix[0])
8        dp = [[0]*n for _ in range(m)]
9        total = 0
10
11        for i in range(m):
12            for j in range(n):
13                if matrix[i][j] == 1:
14                    if i == 0 or j ==0:
15                        dp[i][j] = 1
16                    else:
17                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
18                total += dp[i][j]
19        return total