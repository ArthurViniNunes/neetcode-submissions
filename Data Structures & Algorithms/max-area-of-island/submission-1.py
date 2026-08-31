class Solution:
    lines = 0
    cols = 0
    atual = 0
    def markIsland(self, grid, i, j):
        if self.lines > i >= 0 and self.cols> j >= 0:
            if grid[i][j] != 1:
                return 
            
            grid[i][j] = 2
            self.atual += 1
            self.markIsland(grid, i-1, j)
            self.markIsland(grid, i+1, j)
            self.markIsland(grid, i, j-1)
            self.markIsland(grid, i, j+1)

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        m = 0
        self.lines = len(grid)
        self.cols = len(grid[0])
        for i in range(self.lines):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    self.markIsland(grid, i, j)
                    m = max(m, self.atual)
                    self.atual = 0
        return m