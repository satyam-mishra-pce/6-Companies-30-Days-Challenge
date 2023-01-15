class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])
        for row in dungeon:
            row.append(inf)
        dungeon.append([inf] * n)
        dungeon[~0][~0], dungeon[~1][~0] = 1, 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                best = min(dungeon[i + 1][j], dungeon[i][j + 1])
                dungeon[i][j] = max(1, best - dungeon[i][j])

        return dungeon[0][0]
