class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        result = r
        while l <= r:
            m = (l+r)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/m)
            if hours <= h:
                result = m
                r = m-1
            elif hours > h:
                l = m+1

        return result


        