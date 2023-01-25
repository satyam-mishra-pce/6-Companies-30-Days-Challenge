class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        mat.insert(0, [0] * n)
        for i in range(m + 1):
            mat[i].insert(0, 0)
        m, n = m + 1, n + 1
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
            for j in range(1, n):
                mat[i][j] += mat[i - 1][j]

        def getSumInRange(topleft, bottomright):
            y1, x1 = topleft
            y2, x2 = bottomright

            return mat[y2][x2] - (mat[y1 - 1][x2] + mat[y2][x1 - 1] - mat[y1 - 1][x1 - 1])


        ans = []
        for i in range(1, m):
            ans.append([])
            for j in range(1, n):
                top_left = (max(1, i - k), max(1, j - k))
                bottom_right = (min(m - 1, i + k), min(n - 1, j + k))
                ans[~0].append(getSumInRange(top_left, bottom_right))
        
        return ans
