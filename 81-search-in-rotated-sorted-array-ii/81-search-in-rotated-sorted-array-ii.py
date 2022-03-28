class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # l, r = 0, len(nums) - 1
        
        def rec_search(l, r):
            # print("l, r", l, r)
            if nums[l] < nums[r] and nums[l] < target < nums[r]:
                while l <= r:
                    mid = (l+r) // 2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
            elif l == r or r - l == 1:
                if nums[l] == target or nums[r] == target:
                    return True
            else:
                mid2 = (l+r) // 2
                if nums[mid2] == target:
                    return True
                return rec_search(l, mid2-1) or rec_search(mid2+1, r)
                    
        return rec_search(0, len(nums)-1)
                