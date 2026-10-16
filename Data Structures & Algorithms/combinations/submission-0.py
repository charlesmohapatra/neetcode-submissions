class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answerSet = []
        self.helper(1, [], answerSet, n, k)
        return answerSet
    
    def helper(self, i, currComb, answer, n, k):
        if len(currComb) == k:
            answer.append(currComb.copy())
            return
        if i > n:
            return
        
        for j in range(i, n+1):
            currComb.append(j)
            self.helper(j+1, currComb, answer, n, k)
            currComb.pop()
        