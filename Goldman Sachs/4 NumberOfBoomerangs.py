class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        if len(points) < 3:
            return 0
        
        boomerangs = 0
        for i in range(len(points)):
            distdict = dict()
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if dist not in distdict:
                    distdict[dist] = 1
                else:
                    distdict[dist] += 1
            for dist in distdict:
                boomerangs += distdict[dist] * (distdict[dist] - 1)
        return boomerangs
