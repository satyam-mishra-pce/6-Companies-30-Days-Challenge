class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            area = 0
            if grid[i][j]:
                area += 1
                grid[i][j] = 0
                for x, y in moves:
                    area += dfs(i + x, j + y)
            return area
        
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxarea = max(dfs(i, j), maxarea)
        
        return maxarea
