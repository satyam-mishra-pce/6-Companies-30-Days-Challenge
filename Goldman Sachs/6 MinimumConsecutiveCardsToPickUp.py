class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mindiff = inf
        indexdict = dict()
        for index, card in enumerate(cards):
            if card not in indexdict:
                indexdict[card] = index
            else:
                mindiff = min(mindiff, index + 1 - indexdict[card])
                indexdict[card] = index
        
        if mindiff == inf:
            return -1
        return mindiff
