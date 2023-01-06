class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        cornerset = set()
        sumofareas = 0
        def getArea(xi, y1, ai, bi):
            return (ai - xi) * (bi - yi)
        
        for xi, yi, ai, bi in rectangles:
            sumofareas += getArea(xi, yi, ai, bi)
            cornerset ^= {(xi, yi), (xi, bi), (ai, yi), (ai, bi)}

        if len(cornerset) != 4:
            return False
        
        xi, yi = min(cornerset, key=lambda t: sum(t))
        ai, bi = max(cornerset, key=lambda t: sum(t))
        fullarea = getArea(xi, yi, ai, bi)
        
        return fullarea == sumofareas