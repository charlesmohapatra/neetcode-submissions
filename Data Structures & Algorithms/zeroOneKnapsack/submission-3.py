class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]
        profit = self.dfsHelper(0,profit, weight, capacity, cache)
        return profit
    
    def dfsHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        #exclude item i
        cache[i][capacity] = self.dfsHelper(i+1, profit, weight, capacity, cache)

        #include item i
        newCap = capacity - weight[i]
        if newCap >= 0:
            include = profit[i] + self.dfsHelper(i+1, profit, weight, newCap, cache)
            cache[i][capacity] = max(cache[i][capacity], include)
        return cache[i][capacity]
