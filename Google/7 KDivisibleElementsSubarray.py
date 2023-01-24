class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        l = len(nums)
        divisibles = [not num % p for num in nums]

        ans = 0
        divisiblecountcpy = 0
        for j in range(1, l + 1):
            seen = []
            divisiblecountcpy += divisibles[j - 1]
            divisiblecount = divisiblecountcpy
            for i in range(l + 1 - j):
                if i:
                    divisiblecount += divisibles[i + j - 1] - divisibles[i - 1]
                if divisiblecount <= k:
                    subarr = nums[i : i + j]
                    if subarr not in seen:
                        seen.append(subarr)
            ans += len(seen)

        return ans
        
