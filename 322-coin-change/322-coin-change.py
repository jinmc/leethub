class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            temp_list = []
            for coin in coins:
                if coin < i and dp[i-coin] != -1:
                    temp_list.append(dp[i-coin])
            if temp_list:
                dp[i] = 1 + min(temp_list)
        print(dp)
        return dp[amount]
