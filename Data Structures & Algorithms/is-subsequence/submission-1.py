class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        def check(s,t,l,r):
            if l == len(s):
                return True
            if r == len(t):
                return False
            if s[l] == t[r]:
                l += 1
            r += 1
            return check(s,t,l,r)
        return check(s,t,l,r)