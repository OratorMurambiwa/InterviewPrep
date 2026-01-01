# Last updated: 31/12/2025, 20:30:30
1class Solution(object):
2    def isToeplitzMatrix(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: bool
6        """
7        rows, cols = len(matrix), len(matrix[0])
8
9        for i in range(1, rows):
10            for j in range(1, cols):
11                if matrix[i][j] != matrix[i-1][j-1]:
12                    return False
13        return True