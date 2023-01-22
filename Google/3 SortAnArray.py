class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        from heapq import heapify, heappop
        heapify(nums)

        return [heappop(nums) for i in range(len(nums))]