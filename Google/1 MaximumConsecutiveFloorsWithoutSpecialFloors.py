class Solution:
    def maxConsecutive(self, bottom: int, top: int, specials: List[int]) -> int:
        
        specials.sort()

        maxscore = top - specials[~0]

        for special in specials:
            maxscore = max(maxscore, special - bottom)
            bottom = special + 1
        
        return maxscore