class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        distinct_list = list(set(nums))
        distinct_list.sort()
        dp = [0] * len(distinct_list)
        
        if len(dp) < 2:
            return sum(nums)
        
        dp[0] = nums.count(distinct_list[0]) * distinct_list[0]
        if distinct_list[1] - distinct_list[0] == 1:
            dp[1] = max(dp[0], nums.count(distinct_list[1]) * distinct_list[1])
        else:
            dp[1] = dp[0] + nums.count(distinct_list[1]) * distinct_list[1]
        # print(distinct_list)
        # print(dp)
        
        for i in range(2, len(dp)):
            if distinct_list[i] - distinct_list[i-1] == 1:
                dp[i] = max(dp[i-1], dp[i-2] + nums.count(distinct_list[i]) * distinct_list[i])
            else:
                dp[i] = dp[i-1] + nums.count(distinct_list[i]) * distinct_list[i]
        # print(sorted(nums))
        # print(dp)
        return dp[-1]        