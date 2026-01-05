# Last updated: 04/01/2026, 21:14:51
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True