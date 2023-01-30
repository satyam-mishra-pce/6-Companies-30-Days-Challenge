class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = len(nums1), len(nums2)
        maxlen = 0
        ptrstart1, ptrend1, ptrstart2, ptrend2 = n - 1, n, 0, 1

        while ptrstart1 != ptrend1:
            subarr_len = 0
            for i in range(ptrend1 - ptrstart1):
                if nums1[ptrstart1 + i] == nums2[ptrstart2 + i]:
                    subarr_len += 1
                    maxlen = max(maxlen, subarr_len)
                else:
                    subarr_len = 0

            if ptrstart1:   #if ptrstart1 != 0
                ptrstart1 -= 1
                ptrend2 += 1
            else:
                ptrstart2 += 1
                if ptrend2 == m:
                    ptrend1 -= 1
                else:
                    ptrend2 += 1
        
        return maxlen