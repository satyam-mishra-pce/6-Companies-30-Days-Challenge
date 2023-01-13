class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        curr = 1
        k -= 1
        
        while k > 0:
            levels = 0
            temp_curr = curr
            next_curr = curr + 1
            
            while temp_curr <= n:
                levels += min(n + 1, next_curr) - temp_curr
                temp_curr *= 10
                next_curr *= 10
            
            if levels <= k:
                curr += 1
                k -= levels
            else:
                curr *= 10
                k -= 1
                
        return curr	
