class Solution:
    def findMaxElementIndex(self,mountain_arr, r):
        l = 0
        ans = -1
        while l != r:
            m = l + (r - l) // 2
            if mountain_arr.get(m) > mountain_arr.get(m + 1):
                ans = m
                r = m
            else:
                l = m + 1
        return ans
        
    def binary_search(self, l, r, mountain_arr, key):
        isAssending = mountain_arr.get(l) < mountain_arr.get(r)
        while l <= r:
            m = l + (r - l) // 2
            if mountain_arr.get(m) == key:
                return m
            
            if isAssending:
                if mountain_arr.get(m) < key:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if mountain_arr.get(m) > key:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        
    def findInMountainArray(self, key: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length() - 1
        maxElementIndex = self.findMaxElementIndex(mountain_arr, length)
        found = self.binary_search(0, maxElementIndex, mountain_arr, key)
        if found != -1:
            return found
        return self.binary_search(maxElementIndex + 1, length,mountain_arr, key)
