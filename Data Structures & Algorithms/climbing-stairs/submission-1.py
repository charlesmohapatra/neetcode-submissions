class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1,2]
        i = 3
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i = i+1
        return dp[1]
        