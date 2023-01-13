class Solution:

    def magicalString(self, n: int) -> int:
        
        def createArray(arr, ptr, l):
            if len(arr) >= l:
                return arr
                
            last = arr[~0]
            nextnum = 2
            if last == 2:
                nextnum = 1
            arr.append(nextnum)
            occ = arr[ptr]
            arr.extend([nextnum] * (occ - 1))
            return createArray(arr, ptr + 1, l)
        
        return createArray([1], 1, n)[:n].count(1)
        
