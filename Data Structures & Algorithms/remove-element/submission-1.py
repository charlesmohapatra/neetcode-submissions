class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l = l+1
        print(l)
        print(f"Array is: {nums}")
        return l