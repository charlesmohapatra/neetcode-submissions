class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbery(nums, curr, cache):
            if curr >= len(nums):
                return 0
            if curr in cache:
                return cache[curr]
            cache[curr] = max(nums[curr] + robbery(nums,curr+2, cache), robbery(nums,curr+1, cache))
            return cache[curr]
        
        ans = robbery(nums, 0, {})
        return ans
        