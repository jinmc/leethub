class Solution:
    # 1 => 1
    # 2 => (1, 1) (2 ) => 2
    # 3 => (1,1,1), (1, 2) (2, 1) => 3
    # 4 => (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2) => 5
    # 5 => (1,1,1,1,1), (1,1,1,2), (1,1,2,1), (1,2,1,1), (1,2,2), (2,1,1,1), (2,2,1), (2,1,2) 8  
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * n
        dp[0]=1
        dp[1]=2
        dp[2]=3
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
    # O(2^N) => O(N)
        