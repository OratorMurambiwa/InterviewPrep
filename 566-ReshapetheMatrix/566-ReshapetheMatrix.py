# Last updated: 04/01/2026, 21:38:16
1class Solution(object):
2    def largestLocal(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: List[List[int]]
6        """
7        n = len(grid)
8        res = [[0]* (n-2) for _ in range(n-2)]
9
10        for i in range(n-2):
11            for j in range(n-2):
12                maxval = 0
13
14                for r in range(i, i+3):
15                    for c in range(j, j+3):
16                        maxval = max(maxval, grid[r][c]) 
17
18                res[i][j] = maxval
19        return res
20        