# Last updated: 28/01/2026, 09:26:42
1class Solution(object):
2    def rotate(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        # n = len(matrix) 
8
9        # for r in range(n):
10        #     for c in range(r+1, n):
11        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
12
13        # for r in range(n):
14        #     for c in range(n//2):
15        #         matrix[r][c], matrix[r][n-c-1] = matrix[r][n-c-1], matrix[r][c]
16
17        matrix.reverse()
18        for i in range(len(matrix)):
19            for j in range(i):
20                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]