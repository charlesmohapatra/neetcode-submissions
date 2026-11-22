class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        small,large = [],[]
        for i in nums:
            heapq.heappush(small,-1 * i)
            if small and large and -1 * small[0] > large[0]:
                val = heapq.heappop(small)
                heapq.heappush(large, -1 * val)
            
            if len(small) > len(large) + 1:
                val = heapq.heappop(small)
                heapq.heappush(large, -1 * val)
            if len(large) > len(small) + 1:
                val = heapq.heappop(large)
                heapq.heappush(small, -1 * val)
        if len(small) > len(large):
            return -1 * small[0]
        elif len(large) > len(small):
            return large[0]
        else:
            return (-1 * small[0] + large[0])/2


        