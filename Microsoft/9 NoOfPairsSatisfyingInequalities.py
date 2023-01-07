class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        from sortedcontainers import SortedList
        import bisect

        #Modified Equation: (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
        diffs = SortedList()
        ans = 0

        for num1, num2 in zip(nums1, nums2):
            ans += diffs.bisect_right(num1 - (num2 - diff))
            diffs.add(num1 - num2)
        return ans