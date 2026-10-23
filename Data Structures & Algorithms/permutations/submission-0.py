class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for n in nums:
            ans_t = []
            for p in answer:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j,n)
                    ans_t.append(pCopy)
            answer = ans_t
        return answer

        