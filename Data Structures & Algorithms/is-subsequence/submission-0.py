class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        if len(s) and not len(t):
            return False
        if not len(s) and not len(t):
            return True
        l = 0
        r = 0
        for n in range(len(t)):
            if l == len(s):
                return True
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
            n += 1
        if l == len(s):
            return True
        return False

        