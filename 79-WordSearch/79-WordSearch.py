# Last updated: 29/12/2025, 03:03:50
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """
        Understand
                Inputs -
                    • board: a 2D grid of characters, size m × n
                    • word: the string we need to find in the grid
                Outputs -
                    • Boolean: True if the word can be found, False otherwise
                Constraints -
                    • Letters must be connected horizontally or vertically (not 
                    diagonally)
                    • Each cell can only be used once per word path
                    • 1 ≤ m, n ≤ 6, so DFS with backtracking is acceptable
                Examples/edge cases -
                    • board = [["A","B","C","E"],
                            ["S","F","C","S"],
                            ["A","D","E","E"]]
                    word = "ABCCED" → True
                    word = "SEE" → True
                    word = "ABCB" → False (cell reuse needed)
                    word = "ABFSAB" → False (nonexistent path)
                    Single cell match → True if matches, else False

            Plan
                HL (DFS Backtracking):
                    1. Record grid dimensions: rows = len(board), cols = len(board[0])
                    2. Create a set 'path' to track visited cells during recursion
                    3. Define dfs(r, c, i):
                        - r, c = current coordinates
                        - i = current index in the word
                        - Base case: if i == len(word), return True (all chars matched)
                        - Boundary checks:
                            * if r < 0 or r >= rows or c < 0 or c >= cols → out of
                             bounds
                            * if board[r][c] != word[i] → mismatch
                            * if (r, c) in path → already used in current path
                            * in any of these cases → return False
                        - Add (r, c) to path (mark visited)
                        - Explore all 4 directions: up, down, left, right
                        - If any recursive call returns True → propagate True
                        - Remove (r, c) from path (backtrack)
                        - Return True if found, else False
                    4. In main loop:
                        - Start dfs from every cell that matches word[0]
                        - If any dfs returns True → return True
                    5. If no starting point leads to a full match → return False

            Time: O(m * n * 4^L) where L = len(word)
                (each cell can branch up to 4 directions)
            Space: O(L) recursion stack depth + O(L) path storage

            Real-World Uses
                • Word puzzle solvers (e.g., Boggle, Scrabble path finders)
                • Pathfinding in robotics or games (grid-based traversal)
                • Image pattern recognition (following connected pixels)
                • Maze-solving algorithms using DFS and backtracking
                • DNA sequence tracing (pattern search in grid-like data)


        """
        rows, columns = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= columns 
            or board[r][c] != word[i] or(r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            path.remove((r,c))

            return res

        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        return False


        