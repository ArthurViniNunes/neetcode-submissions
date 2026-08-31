class Solution:

    def markIsland(self, grid, i, j, lines, cols):
        if lines > i >= 0 and cols> j >= 0:
            if grid[i][j] != "1":
                return grid
            
            grid[i][j] = "2"
            self.markIsland(grid, i-1, j, lines, cols)
            self.markIsland(grid, i+1, j, lines, cols)
            self.markIsland(grid, i, j-1, lines, cols)
            self.markIsland(grid, i, j+1, lines, cols)
            return grid
        

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        lines = len(grid)
        cols = len(grid[0])
        for i in range(lines):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    grid = self.markIsland(grid, i, j, lines, cols)
        return res