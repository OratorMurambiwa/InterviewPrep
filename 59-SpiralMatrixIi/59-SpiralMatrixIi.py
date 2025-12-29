# Last updated: 29/12/2025, 03:03:54
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        topborder = 0
        bottomborder = n - 1
        leftborder = 0
        rightborder = n - 1

        val = 1
        
        while topborder <= bottomborder and leftborder <= rightborder:

            for col in range(leftborder, rightborder + 1):
                matrix[topborder][col] = val
                val += 1

            topborder += 1

            for row in range(topborder, bottomborder + 1):
                matrix[row][rightborder] = val
                val += 1

            rightborder -= 1

            if topborder <= bottomborder:
                for col in range(rightborder, leftborder -1, -1):
                    matrix[bottomborder][col] = val
                    val += 1
                
                bottomborder -= 1

            if leftborder <= rightborder:
                for row in range(bottomborder, topborder-1, -1):
                    matrix[row][leftborder] = val
                    val += 1
                
                leftborder += 1

        return matrix




        