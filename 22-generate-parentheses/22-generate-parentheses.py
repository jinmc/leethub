class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # f(n) = (f(0)) f(n-1) + (f(1)) f(n-2).... (f(n-1)) f(0)
        dp = [[] for i in range(n+1)] # n+1
        dp[0].append('')
        for i in range(n+1):
            for j in range(i):
                # i = 1 j = 0 -> (f(0)) f(0)
                # i = 2 j = 0, 1 -> (f(0))f(1) (f(1))f(0)
                dp[i] += ['('+x+')'+y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]