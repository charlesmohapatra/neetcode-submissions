class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1), len(text2)
        cache = [[-1] * (M) for _ in range (N)]
        return self.dfsHelper(text1, text2, 0,0, cache)
    
    def dfsHelper(self, t1, t2, i, j, cache):
        if i == len(t1) or j == len(t2):
            return 0
        if cache[i][j] != -1:
            return cache[i][j]
        if t1[i] == t2[j]:
            cache[i][j] = 1 + self.dfsHelper(t1,t2, i+1, j+1, cache)
        else:
            cache[i][j] = max(self.dfsHelper(t1,t2,i+1, j, cache), self.dfsHelper(t1, t2, i, j+1, cache))
        return cache[i][j]