class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preFix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            preFix[i + 1] = preFix[i] + nums[i]
        
        for i in range(len(nums)):
            leftsum = preFix[i]
            rightsum = preFix[len(nums)] - preFix[i+1]
            if leftsum == rightsum:
                return i
        return -1


        