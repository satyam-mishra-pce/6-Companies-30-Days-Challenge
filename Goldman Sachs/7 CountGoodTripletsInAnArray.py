class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        import bisect
        
        nums2indices = [0] * len(nums2)
        for index, num in enumerate(nums2):
            nums2indices[num] = index
        
        left = []
        right = []
        nums2_pos = []

        for i in range(len(nums1)):
            left.append(bisect.bisect_left(nums2_pos, nums2indices[nums1[i]]))
            nums2_pos.insert(left[-1], nums2indices[nums1[i]])
        
        nums2_pos = []
        for i in range(len(nums1) - 1, -1, -1):
            right.append(bisect.bisect_left(nums2_pos, -nums2indices[nums1[i]]))
            nums2_pos.insert(right[-1], -nums2indices[nums1[i]])
        
        ans = 0
        for i in range(len(left)):
            ans += left[i] * right[len(left) - 1 - i]

        return ans
