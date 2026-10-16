class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currSet, answer = [], []
        self.helper(0, nums, currSet, answer)
        return answer
    
    def helper(self, i, nums, currSet, answer):
        if i >= len(nums):
            answer.append(currSet.copy())
            return
        
        #accept the element
        currSet.append(nums[i])
        self.helper(i+1, nums, currSet, answer)

        #reject the element
        currSet.pop()
        while i+1 < len(nums) and nums[i+1] == nums[i]:
            i += 1
        self.helper(i+1, nums, currSet, answer)
        