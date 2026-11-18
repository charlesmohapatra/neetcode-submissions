class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        ans = self.dfsHelper(0, coins, amount, cache)
        return -1 if ans == float("inf") else ans
    
    def dfsHelper(self, i,  coins, target, cache):
        if target == 0:
            return 0
        if i == len(coins):
            return float("inf")
        if (i, target) in cache:
            return cache[(i, target)]
        res = self.dfsHelper(i+1, coins, target, cache)
        if target - coins[i] >= 0:
            p = 1 + self.dfsHelper(i, coins, target-coins[i], cache)
            res = min(res, p)
        cache[(i, target)] = res
        return res