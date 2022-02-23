class Solution(object):
    def coinChange(self, coins, amount): 
        # amount : m coin개수: n (mxn)
        # O(n ^ m) -> O(nxm)
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue

            temp = None
            for coin in coins:
                if coin < i and dp[i-coin] != -1:
                    if temp is None:
                        temp = dp[i-coin]
                    else:
                        temp = min(temp, dp[i-coin])
            if temp:
                dp[i] = temp + 1
        
        return dp[amount]
        
