class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        s_freqmap = dict()
        for ch in s:
            if ch not in s_freqmap:
                s_freqmap[ch] = 1
            else:
                s_freqmap[ch] += 1
        
        ans = ""
        for ch in order:
            if ch in s_freqmap:
                ans += ch * s_freqmap[ch]
                del s_freqmap[ch]
        
        for ch in s_freqmap:
            ans += ch * s_freqmap[ch]
        
        return ans
