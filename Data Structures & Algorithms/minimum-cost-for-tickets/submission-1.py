class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N,M = len(costs), len(days)
        cache = {}
        return self.dfsHelper(min(days), days, costs, cache)
    
    def dfsHelper(self, i, days, costs, cache):
        if i > max(days):
            return 0
        if i not in days:
            return self.dfsHelper(i+1, days, costs, cache)
        if i in cache:
            return cache[i]
        day_1 = costs[0] + self.dfsHelper(i+1, days, costs, cache)
        day_7 = costs[1] + self.dfsHelper(i+7, days, costs, cache)
        day_30 = costs[2] + self.dfsHelper(i+30, days, costs, cache)
        cache[i] = min(day_1, day_7, day_30)
        return cache[i]
        