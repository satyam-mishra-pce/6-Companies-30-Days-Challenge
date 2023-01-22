class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:

        l = len(statements)
        def validate(perm):
            for i in range(l):
                if not int(perm[i]): continue
                for j in range(l):
                    if statements[i][j] != 2 and statements[i][j] != int(perm[j]): return False
            return True

        ans = 0
        for num in range(1 << l, 1 << (1 + l)):
            perm = bin(num)[3:]
            if validate(perm): 
                ans = max(ans, perm.count('1'))
        return ans