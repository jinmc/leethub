from collections import Counter
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        even_nums = Counter()
        odd_nums = Counter()
        for i in range(len(nums)):
            if i % 2 == 0:
                even_nums[nums[i]] = 1 if nums[i] not in even_nums else even_nums[nums[i]] + 1
            else:
                odd_nums[nums[i]] = 1 if nums[i] not in odd_nums else odd_nums[nums[i]] + 1
        # print(even_nums.most_common(1))
        # print(odd_nums.most_common(1))
        even_nums_total = math.ceil(len(nums) / 2)
        odd_nums_total = len(nums) // 2
        res = len(nums)
        if even_nums.most_common(1)[0][0] != odd_nums.most_common(1)[0][0]:
            res = min(res, even_nums_total - even_nums.most_common(1)[0][1] + odd_nums_total - odd_nums.most_common(1)[0][1])
        else:
            if even_nums.most_common(1)[0][1] <= odd_nums.most_common(1)[0][1]:
                even_remain = even_nums.most_common(2)[1][1] if len(even_nums.most_common(2)) > 1 else 0
                res = min(res, odd_nums_total - odd_nums.most_common(1)[0][1] + even_nums_total - even_remain)
            else:
                odd_remain = odd_nums.most_common(2)[1][1] if len(odd_nums.most_common(2)) > 1 else 0
                res = min(res, odd_nums_total - odd_remain + even_nums_total - even_nums.most_common(1)[0][1])
            
        return res
