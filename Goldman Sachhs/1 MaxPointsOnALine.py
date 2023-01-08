class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        import numpy
        ret = 1

        for i in range(len(points)):
            slopedict = dict()
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    slope = float()
                    if x2 - x1:
                        slope = round((y2 - y1) / (x2 - x1), 10)
                    else:
                        slope = inf
                    intercept = float()
                    if slope == inf:
                        intercept = x1
                    else:
                        intercept = round(y2 - slope * x2, 5)
                    slopehash = str(slope) + " " + str(intercept)
                    if slopehash not in slopedict:
                        slopedict[slopehash] = 1
                    else:
                        slopedict[slopehash] += 1
            maxpoints = 0
            for key in slopedict:
                if slopedict[key] > maxpoints:
                    maxpoints = slopedict[key]
            ret = max(ret, maxpoints + 1)
        
        return ret
                    
