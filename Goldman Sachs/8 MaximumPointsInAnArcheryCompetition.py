class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        reqdArrows = [arrow + 1 for arrow in aliceArrows]
        ans = []
        maxscore = -1

        def recursion(arrows, score, shooted):

            if score == 0 or arrows == numArrows:
                nonlocal maxscore, ans
                if sum(shooted) > maxscore:
                    ans = list(shooted)
                    maxscore = sum(shooted)
                return

            if arrows + reqdArrows[score] <= numArrows:
                arrows += reqdArrows[score]
                shooted.append(score)
            
            for i in range(score - 1, -1, -1):
                newarrows = arrows
                newshooted = list(shooted)
                recursion(newarrows, i, newshooted)
        
        for i in range(11, -1, -1):
            recursion(0, i, [])

        ret = [0] * 12
        shot = 0
        for score in ans:
            ret[score] = reqdArrows[score]
            shot += ret[score]

        ret[0] = numArrows - shot
        return ret
