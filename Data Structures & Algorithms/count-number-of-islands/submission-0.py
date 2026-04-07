class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val == '1':
                    self.bfs(grid, i,j)
                    count += 1
        return count

    def bfs(self, grid, row, col):
        if row < 0 or row > len(grid)-1:
            return
        elif col < 0 or col > len(grid[0])-1:
            return
        else:
            if grid[row][col] == '1':
                grid[row][col] = '0'
                self.bfs(grid, row+1, col)
                self.bfs(grid, row-1, col)
                self.bfs(grid, row, col+1)
                self.bfs(grid, row, col-1)