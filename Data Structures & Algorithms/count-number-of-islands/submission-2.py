class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Input validation: If grid is empty
        if not grid:
            return 0
        
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
    
        def dfs(r,c):
            # if out of bounds or visited
            if (r not in range(rows) or
                c not in range(cols) or 
                grid[r][c] == "0"):
                return
            # change cell to visited
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)

                       

        # Check each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If find a "1" and it has not been visited
                if grid[r][c] == "1":
                    # Run BFS from that cell - BFS will mark all components of the island as visited
                    dfs(r, c)
                    # Since we have not visited this, increment the number of island
                    islands += 1
        return islands

        