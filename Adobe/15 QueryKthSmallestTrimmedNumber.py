class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        digits = []
        for num in nums:
            digits.append([int(digit) for digit in num])
        
        ans = []
        for pos, trimmer in queries:
            sorteddigits = [(item[~(trimmer - 1):], index) for index, item in enumerate(digits)]
            sorteddigits.sort()
            ans.append(sorteddigits[pos - 1][1])
        return ans
