class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N,M = len(word1), len(word2)
        cache = [[-1]* M for _ in range(N)]
        return self.dfsHelper(word1, word2, 0, 0, cache)
    
    def dfsHelper(self,w1,w2,i,j, cache):
        if i == len(w1):
            return len(w2) - j
        elif j == len(w2):
            return len(w1) - i
        if cache[i][j] != -1:
            return cache[i][j]
        
        if w1[i] == w2[j]:
            cache[i][j] = self.dfsHelper(w1,w2,i+1,j+1, cache)
        else:
            cache[i][j] = 1 + min(self.dfsHelper(w1,w2,i,j+1, cache), self.dfsHelper(w1,w2,i+1,j, cache), self.dfsHelper(w1,w2,i+1,j+1,cache))
        return cache[i][j]
