class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        dp = [[0] * (M+1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = 0
        for j in range(M+1):
            if j >= weight[0]:
                dp[0][j] = profit[0]
            else:
                dp[0][j] = 0
        for i in range(1, N):
            for j in range(1, M+1):
                #skip
                skip = dp[i-1][j]
                include = 0
                #not skip
                if j - weight[i] >= 0:
                    include = profit[i] +  dp[i-1][j-weight[i]]

                dp[i][j] = max(skip, include)
        return dp[N-1][M]
        
