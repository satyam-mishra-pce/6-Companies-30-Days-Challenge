class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        from heapq import heapify, heappush
        m, n = len(grid), len(grid[0])

        def countrhombusfromtop(i, size):
            rowsreqd = i + (size * 2 - 1)
            if rowsreqd > m:
                return []
            maxsum = []
            for j in range(n):
                if j - size < -1 or j + size > n:
                    continue
                rhombussum = 0
                coldiff = 0
                for rowdiff in range(size * 2 - 1):
                    if rowdiff == 0:
                        rhombussum += grid[i + rowdiff][j]
                        coldiff += 1
                    elif rowdiff == size * 2 - 2:
                        rhombussum += grid[i + rowdiff][j]
                    elif rowdiff < size:
                        rhombussum += grid[i + rowdiff][j - coldiff] + grid[i + rowdiff][j + coldiff]
                        coldiff += 1
                        if coldiff == size:
                            coldiff -= 2
                    else:
                        rhombussum += grid[i + rowdiff][j - coldiff] + grid[i + rowdiff][j + coldiff]
                        coldiff -= 1
                maxsum.append(-rhombussum)
            return maxsum
        
        allsums = []
        for size in range(1, min((m + 1) // 2, (n + 1) // 2) + 1):
            for row in range(m):
                allsums = allsums + countrhombusfromtop(row, size)
        
        heapify(allsums)
        ret = set()
        while len(ret) < 3:
            if allsums == []:
                break
            ret.add(-heappop(allsums))
        return sorted(list(ret), reverse = True)
