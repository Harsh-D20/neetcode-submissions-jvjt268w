class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = self.bfs(grid, i, j)
                    max_area = max(area, max_area)
    
        return max_area
    
    def bfs(self, grid, i, j):
        if i not in range(0, len(grid)):
            return 0
        if j not in range(0, len(grid[0])):
            return 0
        
        if grid[i][j] == 1:
            grid[i][j] = 0
            left_area = self.bfs(grid, i, j-1)
            right_area = self.bfs(grid, i, j+1)
            top_area = self.bfs(grid, i-1, j)
            bottom_area = self.bfs(grid, i+1, j)
            return 1 + left_area + right_area + top_area + bottom_area
        else:
            return 0