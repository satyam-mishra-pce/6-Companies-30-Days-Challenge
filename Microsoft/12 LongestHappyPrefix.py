class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ""
        
        prefixarray = [0] * len(s)
        relative = 0
        absolute = 1

        while absolute < len(s):
            if s[relative] == s[absolute]:
                relative += 1
                prefixarray[absolute] = relative
                absolute += 1
            else:
                if not relative:
                    absolute += 1
                else:
                    relative = prefixarray[relative - 1]
        return s[:prefixarray[-1]]