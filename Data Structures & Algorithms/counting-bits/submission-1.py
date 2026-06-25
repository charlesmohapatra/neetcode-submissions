class Solution:
    def countNoOfOnes1(self, n) -> int:
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n = n >> 1
        return ans
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1 #Most significant Bit#
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

        