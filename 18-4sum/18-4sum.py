class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a in range(len(nums)-3): # 4개를 계산
            avg = target // 4
            # optimization
            if nums[a] > avg or nums[-1] < avg or (a > 0 and nums[a] == nums[a-1]):
                continue
                
            for b in range(a+1,len(nums)-2):
                avg2 = (target - nums[a]) // 3
                # optimization
                if b > a + 1 and nums[b] == nums[b-1] or (nums[b] > avg2 or nums[-1] < avg2):
                    continue

                # nums[a] + nums[b] + nums[c] + nums[d] == target
                c, d = b+1, len(nums)-1
                while c < d:
                    this_sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if this_sum == target:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif this_sum < target:
                        c += 1
                    else:
                        d -= 1
        return list(result)