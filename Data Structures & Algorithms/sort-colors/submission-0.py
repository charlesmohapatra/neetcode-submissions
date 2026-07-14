class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for i in range(len(nums)):
            count[nums[i]] += 1
        p = 0
        for j in range(len(count)):
            for k in range(count[j]):
                nums[p] = j
                p += 1
        return nums
        