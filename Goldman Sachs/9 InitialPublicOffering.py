class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        from heapq import heappush, heappop
        
        zipped = list(zip(capital, profits))
        zipped.sort()

        profitheap = []
        ptr = 0

        while k:
            while ptr < len(profits) and zipped[ptr][0] <= w:
                heappush(profitheap, -zipped[ptr][1])
                ptr += 1

            if profitheap:
                w -= heappop(profitheap)
            else:
                break        
            k -= 1

        return w
