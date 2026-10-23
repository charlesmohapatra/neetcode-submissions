class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for n in nums:
            ans_t = []
            for p in answer:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    if pCopy not in ans_t:
                        ans_t.append(pCopy)
            answer = ans_t
        return answer
        