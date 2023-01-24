class Solution:

    def __init__(self, w: List[int]):
        self.distribution = []
        prefixsum = 0
        for weight in w:
            prefixsum += weight
            self.distribution.append(prefixsum)
        self.prefixsum = prefixsum

    def pickIndex(self) -> int:
        import bisect
        import random
        return bisect.bisect_left(self.distribution, random.randint(1, self.prefixsum))
