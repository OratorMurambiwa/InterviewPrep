# Last updated: 29/12/2025, 03:03:22
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        Understand  
            Inputs - grid (2D list of strings: "1" = land, "0" = water)  
            Outputs - total number of islands (groups of connected "1"s)  
            Constraints - adjacency is vertical/horizontal only; grid may be empty  
            Edge cases - empty grid, all water, all land, single isolated "1"  

        Plan  
            HL:  
            1. If grid is empty, return 0 immediately.  
            2. Initialize dimensions (rows, cols), a visited set, and island counter.  
            3. Define a BFS function that:  
            - Starts from a land cell (r, c).  
            - Uses a queue to explore all connected land cells.  
            - Marks each visited land cell so it's not counted twice.  
            4. Loop through every cell in the grid:  
            - When you find an unvisited land cell,  
                run BFS to mark the full island and increment total count.  
            5. Return the total number of islands.  

        Time: O(rows × cols) — each cell visited at most once.  
        Space: O(rows × cols) — for visited set and BFS queue.
    """

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        total = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
               
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    total += 1

        return total

                
            
        