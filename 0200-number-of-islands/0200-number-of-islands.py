class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if grid[row][col] == "1":
                grid[row][col] = "0"
                if row > 0:
                    dfs(row - 1, col)
                if col > 0:
                    dfs(row, col - 1)
                if row < len(grid) - 1:
                    dfs(row + 1, col)
                if col < len(grid[row]) - 1:
                    dfs(row, col + 1)
            return

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
    
    
        return result