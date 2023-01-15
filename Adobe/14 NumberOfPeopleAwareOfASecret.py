class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        dp = [-1] * 1001
        def recursion(totaldays):
            
            if totaldays <= 0:
                return 0
            if totaldays <= delay:
                return 1
            people = 1
            if totaldays > forget:
                people = 0
            if dp[totaldays] == -1:
                for i in range(min(totaldays - delay, forget - delay)):
                    people += recursion(totaldays - delay - i)
                dp[totaldays] = people
            return dp[totaldays]
        
        return recursion(n) % (1000000007)
