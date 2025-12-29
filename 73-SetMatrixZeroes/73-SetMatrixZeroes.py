# Last updated: 29/12/2025, 03:03:53
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        """
    Understand  
        Inputs - A 2D list (matrix) of integers that must be modified in place.  
        Outputs - Nothing is returned; all rows and columns containing any 0 are set to 0.  
        Constraints - Must use constant (O(1)) extra space.  
        Edge cases - Zeros in the first row or first column require special handling.  

    Plan  
        HL:  
        1. Find zeros in the matrix and mark corresponding row and column by setting 
           the first cell of that row and column to 0.  
        2. Use an extra boolean (rowZ) to remember if the first row needs to be zeroed.  
        3. After marking, traverse again (skipping first row and column) 
           and set cells to 0 if their row or column is marked.  
        4. Finally, handle first column using matrix[0][0] 
           and handle first row using rowZ flag.  

    Time: O(m × n) — each cell is checked a constant number of times.  
    Space: O(1) — only one boolean variable is used beyond the matrix itself.
        """


        
        rows, cols = len(matrix), len(matrix[0])
        rowZ = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZ = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZ:
            for c in range(cols):
                matrix[0][c] = 0