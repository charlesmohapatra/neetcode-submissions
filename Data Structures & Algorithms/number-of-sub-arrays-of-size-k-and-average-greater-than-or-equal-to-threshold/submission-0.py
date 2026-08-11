class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        maxSum = k * threshold
        L = 0
        currSum = 0
        ans = 0
        for R in range(len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            currSum += arr[R]
            if currSum >= maxSum and R - L + 1 == k:
                ans += 1
        return ans
        