class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if (not k) or n >= k + maxPts:
            return 1
        
        dp = [1] + [0] * n
        ptsSum = 1
        for i in range(1, n + 1):
            dp[i] = ptsSum / maxPts

            if i < k:
                ptsSum += dp[i]
            if i - maxPts >= 0:
                ptsSum -= dp[i - maxPts]
        return sum(dp[k:])
