class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        l, r = 0, len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                result[i] = nums[r] * nums[r]
                r -= 1
            else:
                result[i] = nums[l] * nums[l]
                l += 1
        
        return result