class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_items = {}
        for i in range(len(nums)):
            map_items[nums[i]] = 1 + map_items.get(nums[i],0)
        ans = []
        heapq.heapify(ans)
        for i in map_items.keys():
            heapq.heappush(ans, (map_items.get(i), i))
            if len(ans) > k:
                heapq.heappop(ans)
        ans = [k[1] for k in ans]
        return ans

        
        
        