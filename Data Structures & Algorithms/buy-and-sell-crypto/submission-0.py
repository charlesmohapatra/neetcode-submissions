class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, counter, hold = 0, 0, 0
        def answer(profit, prices, counter, hold):
            if counter >= len(prices):
                return 0
            if hold:
                return max(profit+prices[counter], answer(profit, prices, counter+1, hold))
            #buy
            return max(answer(profit-prices[counter], prices, counter+1,1), answer(profit, prices, counter+1, 0))
            
        return answer(profit, prices, counter, hold)