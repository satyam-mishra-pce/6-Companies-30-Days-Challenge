class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        targetsum = sum(nums) / k
        if sum(nums) % k:
            return False
        nums.sort(reverse = True)
        n = len(nums)
        visited = [0] * len(nums)
 
        def recursion(i = 0, k = k, subsetsum = 0):
            
            if k == 1:
                return True
            if subsetsum == targetsum:
                return recursion(0, k - 1, 0)

            nonlocal visited
            for j in range(i, n):
                if j and (not visited[j - 1]) and nums[j] == nums[j - 1]:
                    continue
                if visited[j] or subsetsum + nums[j] > targetsum:
                    continue
                visited[j] = True
                if recursion(j + 1, k, subsetsum + nums[j]): return True
                visited[j] = False
            
            return False
        
        return recursion()
