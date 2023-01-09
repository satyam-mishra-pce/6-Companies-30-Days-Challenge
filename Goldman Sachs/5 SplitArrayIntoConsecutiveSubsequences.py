class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        lastvaluedict = dict()

        for num in nums:
            
            if not lastvaluedict:
                lastvaluedict[num] = [1]
                continue
            if num - 1 in lastvaluedict:
                lengths = lastvaluedict[num - 1]
                i = 0
                while True:
                    if lengths[i] < 3:
                        break
                    i += 1
                    if i == len(lengths):
                        i -= 1
                        break
                
                if num in lastvaluedict:
                    lastvaluedict[num].append(lengths[i] + 1)
                else:
                    lastvaluedict[num] = [lengths[i] + 1]
                del lastvaluedict[num - 1][i]
                if lastvaluedict[num - 1] == []:
                    del lastvaluedict[num - 1]
            else:
                if num in lastvaluedict:
                    lastvaluedict[num].append(1)
                else:
                    lastvaluedict[num] = [1]
        
        for key in lastvaluedict:
            for length in lastvaluedict[key]:
                if length < 3:
                    return False
        return True
