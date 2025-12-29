# Last updated: 29/12/2025, 03:03:59
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []

        toprowborder = 0
        bottomrowborder = len(matrix) -1
        leftcolborder = 0
        rightcolborder = len(matrix[0]) -1

        while toprowborder <= bottomrowborder and leftcolborder <= rightcolborder:

            for col in range(leftcolborder, rightcolborder + 1):
                res.append(matrix[toprowborder][col])

            toprowborder += 1

            for row in range(toprowborder, bottomrowborder + 1):
                res.append(matrix[row][rightcolborder])

            rightcolborder -= 1

            if toprowborder <= bottomrowborder:
                for col in range(rightcolborder, leftcolborder-1, -1):
                    res.append(matrix[bottomrowborder][col])

                bottomrowborder -= 1

            if leftcolborder <= rightcolborder:
                for row in range(bottomrowborder, toprowborder -1, -1):
                    res.append(matrix[row][leftcolborder])

                leftcolborder += 1

        return res

        