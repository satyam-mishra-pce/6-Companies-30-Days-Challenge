class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        invalidmax, invalidmin = nums[-1], nums[0]
        start, end = -1, -1

        for i in range(1, len(nums)):
            if invalidmin <= nums[i]:
                invalidmin = nums[i]
            else:
                end = i

        for i in range(len(nums) - 2, -1, -1):
            if invalidmax >= nums[i]:
                invalidmax = nums[i]
            else:
                start = i
        
        if start == -1:
            return 0
        return end + 1 - start