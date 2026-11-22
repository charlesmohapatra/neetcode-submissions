class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N,M = len(coins), amount
        cache = [[-1] * (M+1) for _ in range(N)]
        return self.dfsHelper(0,amount,coins, cache)
    
    def dfsHelper(self,i, amount, coins, cache):
        if amount == 0:
            return 1
        if i == len(coins):
            return 0
        if cache[i][amount] != -1:
            return cache[i][amount]
        
        #skip
        ans1 = self.dfsHelper(i+1, amount, coins, cache)
        ans2 = 0

        #add
        if amount - coins[i] >= 0:
            ans2 = self.dfsHelper(i, amount-coins[i], coins, cache)
        cache[i][amount] = ans1 + ans2
        return cache[i][amount]
            
        