class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        rev = lambda x : int(str(x)[::-1])
        diffs = [num - rev(num) for num in nums]
        pairs = 0
        diff_dict = dict()
        for i in range(len(diffs)):
            if diffs[~i] not in diff_dict:
                diff_dict[diffs[~i]] = 1
            else:
                pairs += diff_dict[diffs[~i]]
                diff_dict[diffs[~i]] += 1
        return pairs % 1000000007
