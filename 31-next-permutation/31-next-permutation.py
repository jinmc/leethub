class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        first_increase = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                first_increase = i - 1
                break
        print(first_increase)
        if first_increase == -1:
            nums.sort()
            return
        next_big = nums[first_increase + 1]
        next_big_idx = first_increase + 1
        for j in range(first_increase, len(nums)):
            if nums[j] > nums[first_increase] and nums[j] < next_big:
                next_big = nums[j]
                next_big_idx = j
        temp = nums[first_increase]
        nums[first_increase] = nums[next_big_idx]
        nums[next_big_idx] = temp
        nums[first_increase + 1:] = sorted(nums[first_increase + 1:])
        