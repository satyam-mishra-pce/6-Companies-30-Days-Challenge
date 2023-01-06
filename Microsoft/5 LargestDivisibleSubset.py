class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.append(1)
        nums.sort()
        dp_array = [(0, -1)] * len(nums)

        print(nums)
        def dp(curr = 0):

            nonlocal dp_array
            if curr >= len(nums) - 1:
                return 0

            for i in range(curr + 1, len(nums)):
                if not nums[i] % nums[curr]:
                    new_len = 0
                    if dp_array[i][1] == -1:
                        new_len = dp(i) + 1
                    else:
                        new_len = dp_array[i][0] + 1
                    if dp_array[curr][0] < new_len:
                        dp_array[curr] = (new_len, i)
            return dp_array[curr][0]
        dp()
        
        ans = []
        i = 0
        while dp_array[i][0]:
            ans.append(nums[dp_array[i][1]])
            i = dp_array[i][1]
        return ans

