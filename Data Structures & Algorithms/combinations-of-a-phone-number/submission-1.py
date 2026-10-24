class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        curr = ''
        if len(digits) == 0:
            return ans
        def helper(i, curr, ans):
            if i == len(digits):
                ans.append(curr)
                return
            temp_arr = hash_map[digits[i]]
            for k in temp_arr:
                helper(i+1, curr+k, ans)
        helper(0, curr, ans)
        return ans


