class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        result_arr = [0] * n
        result_arr[0] = 1
        result_arr[1] = 2
        for i in range(2, n):
            result_arr[i] = result_arr[i-1] + result_arr[i-2]
        return result_arr[n-1]
        