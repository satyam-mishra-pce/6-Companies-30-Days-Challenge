class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        substrIndices = set()
        cha, chb, chc = -1, -1, -1
        totalSubstrings = 0

        for i in range(len(s)):
                
            if s[i] == 'a':
                cha = i
            elif s[i] == 'b':
                chb = i
            else:
                chc = i
            
            if cha == -1 or chb == -1 or chc == -1:
                continue
            
            substrStart = min(cha, chb, chc)
            totalSubstrings += 1 + substrStart - len(substrIndices)
            if substrStart not in substrIndices:
                totalSubstrings += len(s) - 1 - max(cha, chb, chc)
            substrIndices.add(substrStart)
        
        return totalSubstrings