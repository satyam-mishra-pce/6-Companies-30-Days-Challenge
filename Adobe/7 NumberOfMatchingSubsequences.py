class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        import bisect

        indexdict = dict()
        for i, ch in enumerate(s):
            if ch not in indexdict:
                indexdict[ch] = [i]
            else:
                indexdict[ch].append(i)
        
        def isSubsequence(letters):
            lastindex = -1
            for letter in letters:
                if letter not in indexdict:
                    return 0
                if lastindex == -1:
                    lastindex = indexdict[letter][0]
                else:
                    left_insertion = bisect.bisect_left(indexdict[letter], lastindex)
                    if left_insertion == len(indexdict[letter]):
                        return 0
                    elif indexdict[letter][left_insertion] == lastindex:
                        left_insertion = bisect.bisect_left(indexdict[letter], lastindex + 1)
                        if left_insertion == len(indexdict[letter]):
                            return 0
                    lastindex = indexdict[letter][left_insertion]
            return 1
        
        ret = 0
        for word in words:
            ret += isSubsequence(word)
        
        return ret
