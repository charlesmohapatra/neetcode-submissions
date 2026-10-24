class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currCombs = []
        combs = []
        def helper(target, nums, combs, currCombs, i):
            if target < 0 or i >= len(nums):
                return
            elif target == 0:
                combs.append(currCombs.copy())
                return
            else: 
                currCombs.append(nums[i])
                helper(target-nums[i], nums, combs, currCombs, i)
                currCombs.pop()
                helper(target, nums, combs, currCombs, i+1)
            
        helper(target, nums, combs, currCombs, 0)
        return combs