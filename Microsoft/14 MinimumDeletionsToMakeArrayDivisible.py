class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        fullgcd = int()
        if len(numsDivide) == 1:
            fullgcd = numsDivide[0]
        else:
            fullgcd = gcd(numsDivide[0], numsDivide[1])
            for i in range(2, len(numsDivide)):
                fullgcd = gcd(fullgcd, numsDivide[i])
        
        nums.sort()
        i = 0
        while i < len(nums):
            if fullgcd % nums[i]:
                i += 1
                continue
            break
        
        if i == len(nums):
            return -1
        return i