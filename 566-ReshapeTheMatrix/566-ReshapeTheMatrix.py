# Last updated: 29/12/2025, 03:02:59
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])

        if m*n != r*c:
            return mat

        flat = []
        for row in mat:
            for val in row:
                flat.append(val)

        res = []
        pointer = 0
        for i in range(r):
            new_row = []
            for j in range(c):
                new_row.append(flat[pointer])
                pointer += 1
            res.append(new_row)

        return res
        