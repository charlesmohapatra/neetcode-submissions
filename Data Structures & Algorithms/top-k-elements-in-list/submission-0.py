class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                num_map[nums[i]] += 1
            else:
                num_map[nums[i]] = 1
        ans = sorted(num_map, key=num_map.get, reverse=True)
        print(ans)
        ans = ans[0:k]
        return ans
        
        