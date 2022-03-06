class Solution:
    def countOrders(self, n: int) -> int:
        
        dp = [1, 6]
        for i in range(3, n+1):
            k = i * 2
            comb = int(k * (k-1) / 2)
            dp.append(comb * dp[-1])
        return dp[n-1] % (10**9 + 7)
        