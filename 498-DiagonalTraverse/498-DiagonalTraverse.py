# Last updated: 29/12/2025, 03:03:05
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        all cells in a diagonal have the same sum for their indicies
        so we can use that to determine even and odd columns
        """
        rows, cols = len(mat), len(mat[0])
        r = c= 0
        res = []

        for _ in range(rows * cols):
            res.append(mat[r][c])

            if (r+c) % 2 == 0: #even so go up and then right
                if c == cols -1:
                    r +=1
                elif r == 0:
                    c +=1
                else:
                    r -=1
                    c +=1

            else: #odd so we go down then left
                if r == rows - 1:
                    c +=1
                elif c == 0:
                    r +=1
                else:
                    r +=1
                    c-=1
        return res

        # rows = len(mat)
        # cols = len(mat[0])

        # res = []

        # cur_row = cur_col = 0
        # going_up = True

        # while len(res) != rows * cols:
        #     if going_up:
        #         # Move up-right
        #         while cur_row >= 0 and cur_col < cols:
        #             res.append(mat[cur_row][cur_col])
        #             cur_row -= 1
        #             cur_col += 1

        #         # Fix overshoot
        #         if cur_col == cols:
        #             cur_row += 2
        #             cur_col -= 1
        #         else:
        #             cur_row += 1

        #         going_up = False

        #     else:
        #         # Move down-left
        #         while cur_row < rows and cur_col >= 0:
        #             res.append(mat[cur_row][cur_col])
        #             cur_row += 1
        #             cur_col -= 1

        #         # Fix overshoot
        #         if cur_row == rows:
        #             cur_col += 2
        #             cur_row -= 1
        #         else:
        #             cur_col += 1

        #         going_up = True

        # return res
