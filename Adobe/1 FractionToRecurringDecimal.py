class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if not numerator: return "0"
        ans = []
        if numerator < 0 < denominator or denominator < 0 < numerator:
            ans.append('-')
            numerator, denominator = abs(numerator), abs(denominator)
        ans.append(str(numerator // denominator))
        rem = numerator % denominator
        if rem:
            ans.append('.')
            places = dict()
            while rem:
                if rem in places:
                    ans.insert(places[rem], "(")
                    ans.append(")")
                    break
                
                places[rem] = len(ans)
                rem *= 10
                ans.append(str(rem // denominator))
                rem = rem % denominator
        
        return ''.join(ans)
