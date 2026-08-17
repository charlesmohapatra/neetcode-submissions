class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        length = 1000000
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if length == 1000000 else length
        