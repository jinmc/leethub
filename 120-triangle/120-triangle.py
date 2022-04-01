class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [triangle[0], [x + triangle[0][0] for x in triangle[1]]]
        for i in range(2, len(triangle)):
            new_arr = list(triangle[i])
            for j in range(len(new_arr)):
                if j == 0:
                    new_arr[j] += dp[i-1][j]
                elif j == len(new_arr)-1:
                    new_arr[j] += dp[i-1][j-1]
                else:
                    new_arr[j] += min(dp[i-1][j], dp[i-1][j-1]) 
            dp.append(new_arr)
        return min(dp[-1])
        