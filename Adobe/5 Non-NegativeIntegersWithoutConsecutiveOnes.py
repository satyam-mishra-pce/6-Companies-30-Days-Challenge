class Solution:
    def findIntegers(self, n: int) -> int:
        
        arr = [1, 2]
        for i in range(2, 32):
            arr.append(arr[~0] + arr[~1])
        
        ans, last, place = 0, 0, 30

        while place >= 0:
            if n & (1 << place):
                ans += arr[place]
                if last: return ans
                last = 1
            else: last = 0
            place -= 1
        
        return ans + 1
