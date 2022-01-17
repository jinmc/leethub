## x = 1000 mid = 500 | 250000

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            if mid ** 2 == x or (mid ** 2 < x and (mid+1) ** 2 > x):
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else: # mid ** 2 < x
                l = mid + 1
        print("exception!")
