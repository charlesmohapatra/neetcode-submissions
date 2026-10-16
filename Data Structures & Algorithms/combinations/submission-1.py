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
        
        currComb.append(i)
        self.helper(i+1, currComb, answer, n, k)

        currComb.pop()
        self.helper(i+1, currComb, answer, n, k)
        