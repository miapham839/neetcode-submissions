class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Input validation: If grid is empty
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0


        def bfs(r, c):
            q = collections.deque()
            # Mark the starting cell as visited
            visited.add((r,c))
            # Add starting cell to queue
            q.append((r,c))

            # While q is not empty
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                # Check the neighbors of this node (4 directions)
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check if the position is valid
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                            # Add to queue to run BFS on this cell as well
                            q.append((r, c))
                            visited.add((r, c))
                       

        # Check each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If find a "1" and it has not been visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Run BFS from that cell - BFS will mark all components of the island as visited
                    bfs(r, c)
                    # Since we have not visited this, increment the number of island
                    islands += 1
        return islands
