class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        cache = {}
        if total % 2 != 0:
            return False
        return self.dfsHelper(0,total//2,n, nums, cache)
    
    def dfsHelper(self, i, total, n, nums, cache):
        if i == n:
            return False
        if total < 0:
            return False
        elif total == 0:
            return True
        if (i, total) in cache:
            return cache[(i, total)]
        #skip
        bool1 = self.dfsHelper(i+1, total, n, nums, cache)
        #include
        bool2 = self.dfsHelper(i+1, total-nums[i], n, nums, cache)
        cache[(i,total)] = bool1 or bool2
        
        return cache[(i,total)]