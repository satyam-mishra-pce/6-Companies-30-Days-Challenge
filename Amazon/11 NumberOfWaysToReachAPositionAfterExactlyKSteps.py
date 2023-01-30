class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        dp = dict()
        def recursion(start, remaining):
            
            if not remaining:
                if start == endPos:
                    return 1
                return 0
            
            remaining -= 1
            
            if start not in dp:
                dp[start] = [inf] * k
                dp[start][remaining] = recursion(start + 1, remaining) + recursion(start - 1, remaining)
            elif dp[start][remaining] == inf:
                dp[start][remaining] = recursion(start + 1, remaining) + recursion(start - 1, remaining)

            return dp[start][remaining]
            
        return recursion(startPos, k) % 1000000007