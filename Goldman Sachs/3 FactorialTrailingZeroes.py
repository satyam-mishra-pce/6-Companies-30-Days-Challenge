class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ans = 0
        exp = 5
        while n >= exp:
            ans += n // exp
            exp *= 5
        return ans
