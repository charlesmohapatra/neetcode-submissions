class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_map = {}
        answer = 0
        for i in range(len(nums)):
            tmp = hash_map.get(nums[i], 0)
            if tmp < 2:
                answer += 1
            else:
                nums[i] = 1000001
            hash_map[nums[i]] = tmp + 1
        nums.sort()
        return answer
        