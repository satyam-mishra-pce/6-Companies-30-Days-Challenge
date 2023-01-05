class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        sumofnums = sum(nums)
        f0 = 0
        for index, num in enumerate(nums):
            f0 += index * num

        ans = f0
        for i in range(1, len(nums)):
            f0 = f0 + sumofnums - nums[len(nums) - i] * len(nums)
            ans = max(ans, f0)

        return ans