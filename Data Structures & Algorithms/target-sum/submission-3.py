class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N,M = len(nums), target
        cache = {}
        return self.dfsHelper(0, nums, target, 0, cache)
    
    def dfsHelper(self, i, nums, target, curr, cache):
        if i == len(nums):
            if curr == target:
                return 1
            else:
                return 0
        if (i, curr) in cache:
            return cache[(i, curr)]
        
        #exclude
        count_exclude = self.dfsHelper(i+1, nums, target, curr-nums[i], cache)


        #include
        count_include = self.dfsHelper(i+1, nums, target, curr+nums[i], cache)
        cache[(i, curr)] = count_exclude + count_include

        return cache[(i, curr)]
        