class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = []
        total = 0
        for i in self.nums:
            total += i
            self.prefixSum.append(total)

        

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefixSum[right]
        preLeft = self.prefixSum[left-1] if left > 0 else 0
        return (preRight - preLeft)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)