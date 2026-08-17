class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        length, L = 0 ,0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            while count[s[R]] > 1:
                count[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length
        