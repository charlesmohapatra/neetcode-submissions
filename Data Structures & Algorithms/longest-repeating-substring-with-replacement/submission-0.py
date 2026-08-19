class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        L = 0
        def helper(obj):
            mx = 0
            for i in obj:
                mx = max(mx, obj[i])
            return mx
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_count = helper(count)
            if (R - L + 1) - max_count <= k:
                res = max(res, R-L+1)
            else:
                count[s[L]] -= 1
                L += 1
        return res


        