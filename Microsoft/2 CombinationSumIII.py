class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []

        def dfs(start, end, combination, prevsum):
            
            if len(combination) == k:
                if sum(combination) == n:
                    ans.append(combination)
                return

            for num in range(start, end + 1):
                dfs(num + 1, end, combination + [num], prevsum + num)

        dfs(1, 9, [], 0)

        return ans