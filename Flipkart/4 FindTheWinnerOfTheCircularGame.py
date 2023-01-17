class Solution:

    def findTheWinner(self, n: int, k: int) -> int:

        def recursion(curr = 0, ingame = [i for i in range(1, n + 1)]):
            if len(ingame) == 1:
                return ingame[0]
            rel_idx = (curr + k - 1) % len(ingame)
            ingame.pop(rel_idx)
            return recursion(rel_idx, ingame)
        
        return recursion()
