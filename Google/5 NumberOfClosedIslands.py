class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return True

            ret = True
            if not grid[i][j]:
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    ret = False
                grid[i][j] = 1
                for xinc, yinc in moves:
                    if not dfs(i + xinc, j + yinc):
                        ret = False
            
            return ret
        
        count = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j] and dfs(i, j):
                    count += 1
        
        return count