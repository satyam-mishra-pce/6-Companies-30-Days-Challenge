class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        noOfPiles = len(piles) // 3
        piles.sort(reverse = True)
        ans = 0
        for i in range(1, len(piles) - noOfPiles, 2):
            ans += piles[i]
        return ans
