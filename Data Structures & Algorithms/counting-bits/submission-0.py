class Solution:
    def countNoOfOnes1(self, n) -> int:
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n = n >> 1
        return ans
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.countNoOfOnes1(i))
        return ans

        