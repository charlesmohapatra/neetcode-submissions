class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        preFix = 1
        postFix = 1
        for i in range(len(nums)):
            ans[i] = preFix
            preFix = preFix * nums[i]
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= postFix
            postFix *= nums[j]
        return ans




        