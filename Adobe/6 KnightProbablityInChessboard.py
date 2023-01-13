class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        possiblemoves = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        dp = [[([-1] * k) for i in range(n)] for j in range(n)]
        
        def recursion(boardsize, moves, r, c):
            nonlocal dp
            if r < 0 or r >= boardsize or c < 0 or c >= boardsize:
                return 0
            if moves == 0:
                return 1
            if dp[r][c][moves - 1] == -1:
                p = 0
                for row, column in possiblemoves:
                    p += recursion(boardsize, moves - 1, r + row, c + column)
                dp[r][c][moves - 1] = p / 8
            return dp[r][c][moves - 1]

        return recursion(n, k, row, column)
