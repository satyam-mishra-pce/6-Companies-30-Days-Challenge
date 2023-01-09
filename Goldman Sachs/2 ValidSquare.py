class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        points = [p1, p2, p3, p4]
        dists = []
        for x1, y1 in points:
            temp_dist = []
            for x2, y2 in points:
                temp_dist.append(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            temp_dist.sort()
            if not temp_dist[1]:
                return False
            if temp_dist[1] != temp_dist[2]:
                return False
            if temp_dist[1] + temp_dist[2] != temp_dist[3]:
                return False
            if dists == []:
                dists = list(temp_dist)
            elif dists != temp_dist:
                return False
        return True
